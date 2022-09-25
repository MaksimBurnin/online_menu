from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Allergen)
class AllergenAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Dish)
class MenuAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass
