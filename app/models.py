from django.db import models
from django.core.validators import validate_email, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position', 'name']


class Allergen(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    allergens = models.ManyToManyField(Allergen)
    energy_value = models.IntegerField()
    price = models.IntegerField(validators=[MinValueValidator(1, "Price should be positive")])
    image = models.ImageField()
    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, validators=[validate_email])
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def fill_from_cart(self, session):
        cart = session.get('cart', {})
        total = 0
        for pk, qty in cart.items():
            dish = Dish.objects.get(pk=pk)
            item = OrderItem(
                order=self,
                dish=dish,
                qty=qty,
            )
            item.save()

    def save(self, *args, **kwargs):
        self.total = 0

        if self.pk:
            items = self.order_items.all()
        else:
            items = []

        for item in items:
          self.total += item.price * item.qty

        super().save(*args, **kwargs)




class OrderItem(models.Model):
    # Basic information of products is dupliated to preserve it for
    # en event of product deletion, or price change
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField(validators=[MinValueValidator(1, "Quantity should be positive")])
    subtotal = models.IntegerField()
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")

    def save(self, *args, **kwargs):
        if self.dish:
          self.name = self.dish.name
          self.price = self.dish.price
          self.subtotal = self.price * self.qty

        super().save(*args, **kwargs)
