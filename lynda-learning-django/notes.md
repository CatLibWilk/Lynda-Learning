# Chpt. 2 Models and Admin

- Django uses Model-View-Controller architecture, but with slightly different components
    - URL patterns, views, models, templates

- URL patterns route requests to appropriate view
- view is the logic-handling portion of architecture
    - can leverage models to query database
- In django, the controller of `MVC` is the "view", and the view of `MVC` is the "template"

## Models
- example usage in `models.py`
```
from django.db import models

class SomeModel( models.Model ):
    name = models.CharField( max_length=100 )
    description = models.CharField( max_length=500 )
```
- Field Types
    - CharField
    - TextField
    - IntegerField
    - DecimalField
    - BooleanField
    - DateTimeField
    - ForeignKey ( value is id of record in other model )
    - ManyToManyField

- CharField vs. TextField
    - CharField requires max_length argument
    - TextField will store variable length string

 - `choices` field attribute can limit input so set of given values
    - create class attribute like `field_choices` with value = a list of 2-tuples giving name of field in DB and its display string
        - ex
        ```
        SEX_CHOICES = [ ( 'M', 'Male' ),( 'F', 'Female' ) ]
        ...
        sex = models.CharField( max_length = 1, choices = SEX_CHOICES )
        ```
- `ManyToManyField`
    - takes name of referenced model as first argument

## Admin
- create custom django-admin commands
    - use `BaseCommand` model from `django.core`
    - add `management/commands` nested directories to a particular app ( eg. `api`, `core` )
        - `manage.py` will have access to any file in this directory that doesn't begin with undercore
    - eg.
    ```
    ## /wisdompets/adoptions/management/commands/load_csv.py

    from csv import DictReader
    from datetime import datetime

    from django.core.management import BaseCommand

    from adoptions.models import Pet, Vaccine
    from pytz import UTC

    class Command(BaseCommand):<---
        # Show this when the user types help
        help = "Loads data from pet_data.csv into our Pet mode"

        def handle(self, *args, **options):
            if Vaccine.objects.exists() or Pet.objects.exists():
                print('Pet data already loaded...exiting.')
                print(ALREDY_LOADED_ERROR_MESSAGE)
                return

            print("Loading pet data for pets available for adoption")
            for row in DictReader(open('./pet_data.csv')):
                pet = Pet()
                pet.name = row['Pet']
                pet.submitter = row['Submitter']
                ...
                pet.save()
     ```
    - invoking command will run the `handle` method of given class

- create admin interface for models (ie. to use in /admin in browser)
- in `admin.py` 
    - `from django-contrib import admin`
    - `from .models import [some model]`
    - create class for admin of given model
    - decorate with @admin.register decorator, passing in name of model as arg
    ```
    from django-contrib import admin
    from .models import Pet

    @admin.register(Pet)
    class PetAdmin(admin.ModelAdmin):
        pass
    ```
- by default, the above class will display list of entries as `[ model_name ] Object [ number ]`
    - need to add `list_display` attr to admin class with columns to show
    ```
    list_display = ['name', 'species', 'breed', 'age', 'sex']
    ```
- To control what is displayed for a given value from linked model (here eg. `Vaccine` ), need to overwrite the `__str__` method of the linked model
    ```
    class Vaccine(models.Model):
        name = models.CharField(max_length=50)

        def __str__(self):
            return self.name
    ```
## Querying with django ORM

- for eg., using `Pet` model
- models have `objects` attr with attached methods for query
- Pet.objects.all() returns `QuerySet` of all entries in table
- `Pet.objects.get( arg )` returns a single instance result
    - .get() not used for non-unique fields
    - arg that applies to multiple records (like `Pet.objects.get( age = 1 )` ) returns `MultipleObjectsReturned` exception
- `Pets.objects.filter( arg )` used for non-unique field arguments
- Querying for data linked by foreign key
    - eg. if a pet has linked vaccinations, `Pet.objects.get( id=7 ).vaccinations.all( )` will return a QuerySet of linked records

# Chpt. 3 URL Handlers and Views
- in urls.py `path` list, the `name` argument for a path is optional, but is used in templates to create links to a particular route
- in the path, anything inside of angle brackets is the `capture group`:
    - first part is the `path converter` tells django what data type to expect
        - eg. <int:id> tells django to expect an integer, so if a string is passed in it wont work
    - second part is the keyword argument 

## views
- import HttpRequest module from django.http
- use `render` function in view to pass data to template
    - render takes:
        - `request` as first argument
        -  string for name of template to use as second
        - data dictionary as third
            - keys of dict must be strings, used in template as variable names

- eg
    ```
    def home( request ):
        pets = Pet.objects.all( )
        return render( request, 'home.html', {
            'pets': pets,
        } )
    ```

- for views that take argument, need to account for data not found
    - wrap ORM call in try/except, using `[Model.DoesNotExist]` in exception
        ```
            try:
                pet = Pet.object.get( id = pet_id )

            except Pet.DoesNotExist:
                raise Http404( 'Pet not found' )
        ```
    - use `Http404` module of `django.http` to raise 404 and define error message

# Chpt. 4 Templates
## elements of syntax
    - variable: {{ variable }}
    - template tag: {% tag %}: used for for-loops, ifs, structural elements, etc.
        - CAN NOT be like so: `{ % tag % }, ie with space between percent sign and bracket
        
    - template filter: {{ variable | filter }}: mostly used to take string and output some formatting 
        - ex. builtin `capfirst` filter `{{ pet.name | capfirst }}` will ensure that output names have first letter capitalized

- loop example
    ```
    {% for pet in pets %}
        <li>{{ pet.name | capfirst }}</li>
    {% endfor %}
    ```
- some template tags don't have end tag
    ex. URL tag: `{% url 'home' %}`: takes name of url pattern as arg and renders the url path as string 
    - for paths that take arg (eg. id), the arg is passed as an additional argument in url tag
        - `{% url 'home' pet.id %}`

## inheritance
- to reduce repetition, django projects typically use a base.html template containing the standard html elements that all pages will use
    - body will contain `{% block content%}{% endblock content%}` tags
- child templates then use `{% extends "base.html" %}` take to inherit, and place content within `{% block content %}{% endblock content %}` tags 

## integrating js/css
- `static` directory should be at same level as `manage.py`
- to `settings.py` add variable:
    ```
        STATICFILES_DIRS = [ 
            os.path.join( BASE_DIR, 'static' )
        ]
    ```
- to implement in template
    - add `{% load static %}` template tag to template
    - change/add href values like so: `...href="{% static 'style.css' %}`
        - an image would look like: `<img src="{% static 'images/header.jpg' %}" alt="Wisdom Pet Medicine">`

## javascript
- add `<script>` tag with `src` = {% static 'file.js' %}