from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, JsonResponse
from django.db import transaction
from rest_framework import viewsets, parsers

from .cart import Cart
from .models import Category, Order, Dish
from .serializers import DishSerializer
from . import forms

class MenuView(View):
    def load_data(self):
        categories = Category.objects.prefetch_related('dishes')
        cart = Cart(self.request.session)
        form = forms.CreateOrderForm(self.request.POST)
        return {'categories': categories, 'order_form': form, 'cart': cart}

    def get(self, request):
        context = self.load_data()
        context['order_form'] = forms.CreateOrderForm()
        return render(request, 'dishes/index.html', context)

    @transaction.atomic
    def post(self, request):
        context = self.load_data()
        form = context['order_form']

        if form.is_valid():
            form.save()
            order = form.instance
            order.fill_from_cart(request.session)
            form.save()

            return redirect('order', order_id=form.instance.pk)
        else:
            return render(request, 'dishes/index.html', context)


def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/show.html', {'order': order})

def cart_action(request):
    if request.method != "POST":
        return HttpResponseBadRequest()

    cart = Cart(request.session)
    action = request.POST['action']
    pk = request.POST['id']

    if action == 'add':
        cart.add(pk)

    if action == 'remove':
        cart.remove(pk)

    return JsonResponse(cart.items)


class ApiDishViewSet(viewsets.ModelViewSet):
    """
    Use [GET] to retrive a list of Dishes, availible in Online Menu,
    or [POST] to create a new one
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
