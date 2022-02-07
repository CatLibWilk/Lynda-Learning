from django.conf import settings
from django.db import models
from django.shortcuts import reverse

DEFAULT_TEXTFIELD_TEXT = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Et dolor suscipit libero eos atque quia ipsa sint voluptatibus! Beatae sit assumenda asperiores iure at maxime atque repellendus maiores quia sapiente."
CATEGORY_CHOICES = (
    ( 'S', 'Shirt' ),
    ( 'SW', 'Sportwear' ),
    ( 'OW', 'Outerwear' ),
)

## supports different colored `bestseller`, 'new item'-type labels on product cards
LABEL_CHOICES = (
    ( 'P', 'primary' ),
    ( 'S', 'secondary' ),
    ( 'D', 'danger' ),
)

class Item( models.Model ):
    title = models.CharField( max_length = 100 )
    price = models.FloatField( null = True )
    category = models.CharField( choices = CATEGORY_CHOICES, default = 'S', max_length = 2 )
    label = models.CharField( choices = LABEL_CHOICES, default = 'P', max_length = 1 )
    slug = models.SlugField( default = 'test-product' )
    description = models.TextField( default = DEFAULT_TEXTFIELD_TEXT )

    def __str__( self):
        return self.title
    
    def get_absolute_url( self ):
        return reverse("core:product", kwargs = {
            'slug': self.slug 
        } )

    def get_add_to_cart_url( self ):
        return reverse("core:add-to-cart", kwargs = {
            'slug': self.slug 
        } )

    def get_remove_from_cart_url( self ):
        return reverse("core:remove-from-cart", kwargs = {
            'slug': self.slug 
        } )


class OrderItem ( models.Model ):
    user = models.ForeignKey( settings.AUTH_USER_MODEL,  on_delete=models.CASCADE )
    ordered = models.BooleanField( default = False )
    
    item = models.ForeignKey( Item, on_delete = models.CASCADE )
    quantity = models.IntegerField( default = 1 )

    def __str__( self ):
        return f"{ self.quantity } of { self.item.title }"
    
    def get_total_item_price( self ):
        return self.quantity * self.item.price

class Order(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL,  on_delete=models.CASCADE )

    items = models.ManyToManyField( OrderItem )
    start_date = models.DateTimeField( auto_now_add = True )
    ordered_date = models.DateTimeField( )
    ordered = models.BooleanField( default = False )
    
    def __str__ ( self ):
        return self.user.username
     
    def get_total( self ):
        total = 0
        for order_item in self.items.all( ):
            total += order_item.get_total_item_price( )
        
        return total