from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, JsonResponse
from django.db import transaction

from .models import Category, Order
from . import forms

class MenuView(View):
    def get(self, request):
        categories = Category.objects.prefetch_related('dishes')
        form = forms.CreateOrderForm()
        context = {'categories': categories, 'order_form': form}
        return render(request, 'dishes/index.html', context)

    @transaction.atomic
    def post(self, request):
        form = forms.CreateOrderForm(request.POST)
        if form.is_valid():
            form.save
            order = form.instance
            order.fill_from_cart(request.session)
            form.save()

            return redirect('order', order_id=form.instance.pk)
        else:
            return render(request, 'dishes/index.html', context)


def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/show.html', {'order': order})

def cart_add(request):
    if request.method != "POST":
        return HttpResponseBadRequest()
    JsonResponse({})

def cart_remove(request):
    if request.method != "POST":
        return HttpResponseBadRequest()
    JsonResponse({})
