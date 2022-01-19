from tracemalloc import get_object_traceback
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .models import Item, OrderItem, Order

class HomeView( ListView ):
    model = Item
    template_name = 'home.html'

class ItemDetailView( DetailView ):
    model = Item
    template_name = 'product.html'

def CheckoutView( request ):
    return render ( request, template_name = 'checkout.html' )

def add_to_cart( request, slug ):
    item = get_object_or_404( Item, slug=slug )
    ##use get_or_create so that ordering an item more than once just changes quantity of existing, not creates new
    order_item, created = OrderItem.objects.get_or_create( 
        item = item,
        user = request.user,
        ordered = False
    )
    order_qs = Order.objects.filter( user = request.user, ordered = False )
    
    if order_qs.exists( ):
        order = order_qs[ 0 ]
        # check if item is already in order
        if order.items.filter( item__slug = item.slug ).exists( ):
            order_item.quantity += 1
            order_item.save( )
        else:
            order.items.add( order_item )

    else:
        ordered_date = timezone.now( )
        order = Order.objects.create( user = request.user, ordered_date = ordered_date )
        order.items.add( order_item )

    return redirect( "core:product", slug = slug )

def remove_from_cart( request, slug ):
    item = get_object_or_404( Item, slug=slug )

    order_qs = Order.objects.filter( user = request.user, ordered = False )
    
    if order_qs.exists( ):
        order = order_qs[ 0 ]
        # check if item is already in order

        if order.items.filter( item__slug = item.slug ).exists( ):
            order_item = OrderItem.objects.filter(
                item = item,
                user = request.user,
                ordered = False
            )[ 0 ]

            order.items.remove( order_item )
        else:
            return redirect( "core:product", slug = slug )    

    else:
        return redirect( "core:product", slug = slug )

    return redirect( "core:product", slug = slug )