## following tutorial: How to Build an E-commerce Website with Django and Python (by freecodecamp)
# Setup
- make venv
- cloned boilerplate at https://github.com/justdjango/django_project_boilerplate.git
- `pip install -r requirements.txt`
- rename main app ( boilerplate has as `demo` )
    - `python manage.py demo [newname]`
- create `static_in_env` directory at same directory level as app, core, etc.
- authentication
    - `pip install django-allauth`
    - follow installation guide in allauth documentation (readthedocs)
        - add configuration to settings.py
        - add url settings
        - `python manage.py migrate`
- create admin user
    - `python manage.py createsuperuser`

# Building Models
 - build models in the `core` app/directory 
 - make `item` `orderitem` and `order` classes
    - the `orderitem` links an item to an order
    - basic modeling:
        ```
        from django.conf import settings
        from django.db import models

        class Item( models.Model ):
            title = models.CharField( max_length = 100 )
            price = models.FloatField( )
            def __str__( self) :
                return self.title

        class OrderItem ( models.Model ):
            item = models.ForeignKey( Item, on_delete = models.CASCADE )
            def __str__( self ):
                return self.title

        class Order(models.Model):
            user = models.ForeignKey( settings.AUTH_USER_MODEL,  on_delete=models.CASCADE )

            items = models.ManyToManyField( OrderItem )
            start_date = models.DateTimeField( auto_now_add = True )
            ordered_date = models.DateTimeField( )
            ordered = models.BooleanField( default = False )
            
            def __str__ ( self ):
                return self.user.username
        ```
    - add to admin config as well
        - import models into admin.py
        - add: `admin.site.register( [model_name] )` for each model
    
- categories
    - create tuple of 2-tuples outside of any model like so, where the first value is what's stored in DB, 2nd is the display value
    ```
        CATEGORY_CHOICES = (
            ( 'S', 'Shirt' ),
            ( 'SW', 'Sportwear' ),
            ( 'OW', 'Outerwear' ),
        )
    ```
    - reference in models like so
    ```
        category = models.CharField( choices=CATEGORY_CHOICES, default = 'S', max_length = 2 )
    ```
    - in templates, can get the display value with `.get_[category_name]_display` function
    ```
        {{ item.get_category_display }}
    ```
# Views
- create `item_list` view like so:
    ```
        from .models import Item, OrderItem, Order

        def item_list( request ):
            context = {
                'items': Item.objects.all( )
            }
            return render( request, 'item_list.html', context )
    ```
- create a `urls.py` in the `core` directory and add a path for the new view
    - must also set `app_name` in the urls file
- in the main app's `urls.py`, add an `includes` statement to route urls from the `core` app
    ```
        urlpatterns = [
            path( 'admin/', admin.site.urls ),
            path( 'accounts/', include( 'allauth.urls' ) ),
            path( '', include( 'core.urls', namespace = 'core' ) )
        ]
    ```
- class-based views can reduce code
    - `from django.views.generic import ListView, DetailView`
    - for a list-based view (like the one displaying all products on homepage)
        ```
            class HomeView( ListView ):
                model = [model_name]
                template_name = 'home.html'
        ```
    - in `urls.py` give as `HomeView.as_view( )` in url path def
    - in templates, the object to loop through is `object_list`
        - eg. `{% for item in object_list %}`

# Templates
- create `item_list.html` in `templates` directory
    ```
        {% extends "base.html" %}

        {% block content %}
            <h2>Here is the list of items</h2>

            {% for item in items %}

                {{ item }}
                
            {% endfor %}

        {% endblock content %}
    ```

# Using mdbootstrap ecommerce template
- https://mdbootstrap.com/freebies/jquery/e-commerce/
- download the template and add the js/css/etc. folders to `static_in_env` 
- add the checkout/homepage/etc .html files to the `templates` directory
- in the template .html files, add `{% load static %}` to top of file
- change hrefs/src attributes in the `<link>` and `<script>` tags to reflect location of files in `static_in_env` directory
    - like so: `src={% static 'js/mdb.min.js' %}`
- may need to confirm that static settings are correct in `settings.py`
    ```
        # Static files (CSS, JavaScript, Images)

        STATIC_URL = '/static/'
        MEDIA_URL = '/media/'
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
        STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
    ```

# building individual product page linking
- need to add `slug` field and `get_absolute_url` method to Item model
    - `slug = models.SlugField( default = 'default' )`
    - method
        ```
            def get_absolute_url( self ):
                return reverse("core:product", kwargs = {
                    'slug': self.slug 
                } )
        ```
        - `reverse` first argument is: namespace (ie. app ) - colon - name given in url definition

- add slug to url def
    - `path('product/<slug>/', ItemDetailView.as_view( ), name='product'),`

- alter href links in templates
    - `href="{{ item.get_absolute_url }}"`


# Adding Items to cart
- basic steps
    - create orderitem from item
    - assign order item to order if user has order/create new if not
    - be able to remove item

- define `add_to_cart` function
    - takes request and slug of item as args
    ```
    def add_to_cart( request, slug ):
        item = get_object_or_404( Item, slug=slug ) !<--- get item object by slug
        ##use get_or_create so that ordering an item more than once just changes quantity of existing, not creates new
        order_item, created = OrderItem.objects.get_or_create( !<----- !
            item = item,
            user = request.user,
            ordered = False
        )
        order_qs = Order.objects.filter( user = request.user, ordered = False ) !<--- see if user has order!
        
        if order_qs.exists( ):
            order = order_qs[ 0 ]
            # check if item is already in order
            if order.items.filter( item__slug = item.slug ).exists( ): !<--- if item already in order, increase quantity
                order_item.quantity += 1
                order_item.save( )
            else: !<--- if item not in order, add to order!
                order.items.add( order_item )

        else: !<--- create order if user doesnt have one !
            ordered_date = timezone.now( )
            order = Order.objects.create( user = request.user, ordered_date = ordered_date )
            order.items.add( order_item )

        return redirect( "core:product", slug = slug ) !<--- after add to order, redirect/refresh to same product page
    ```
- add add_to_cart to urls.py
    ```
    ...
        path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    ...
    ```
-  create `get_add_to_cart_url` shortcut method in Item class
    - returns URL to add to cart with the item's slug
    ```
    def get_add_to_cart_url( self ):
        return reverse("core:add-to-cart", kwargs = {
            'slug': self.slug 
        } )
    ```
- in template, make submit button with `get_add_to_cart_url` in href of <a> tag
    ```
    <a href="{{ object.get_add_to_cart_url }}" class="btn btn-primary btn-md my-0 p">Add to cart
        <i class="fas fa-shopping-cart ml-1"></i>
    </a>
    ```
( to 45:00 )