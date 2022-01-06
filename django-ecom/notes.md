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

( To 15:00 ) - 1/5/22 - Couldn't figure out all the changes that happened between loading the MDN templates and breaking them out into different templates, making the routes, etc ( ie. what's shown between 15 min and the 'add item to cart' title ). Going to take a break from this tutorial and look at a more beginner-friendly one