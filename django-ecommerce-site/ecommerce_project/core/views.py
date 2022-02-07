from tracemalloc import get_object_traceback
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .models import Item, OrderItem, Order

class HomeView( ListView ):
    model = Item
    paginate_by = 10
    template_name = 'home.html'

class ItemDetailView( DetailView ):
    model = Item
    template_name = 'product.html'


class OrderSummaryView( LoginRequiredMixin, View ):
    def get( self, *args, **kwargs ):
        try:
            order = Order.objects.get( user = self.request.user, ordered = False )
            context = {
                'object': order
            }

            return render( self.request, 'order_summary.html', context )
        
        except ObjectDoesNotExist:
            messages.error( self.request, "You don't have an order" )
            return redirect( "/" )

    
def CheckoutView( request ):
    return render ( request, template_name = 'checkout.html' )

@login_required
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
            messages.info( request, "This item quantity was updated in your cart." )
        else:
            messages.info( request, "This item was added to your cart." )
            order.items.add( order_item )

    else:
        ordered_date = timezone.now( )
        order = Order.objects.create( user = request.user, ordered_date = ordered_date )
        order.items.add( order_item )
        messages.info( request, "This item was added to your cart." )

    return redirect( "core:product", slug = slug )

@login_required
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

            order_item.delete( )
            messages.info( request, "This item was removed from your cart." )
            return redirect( "core:product", slug = slug )
        else:
            messages.info( request, "This item was not in your cart." )
            return redirect( "core:product", slug = slug )    
    else:
        messages.info( request, "You do not have an active order." )
        return redirect( "core:product", slug = slug )

