### These are notes for read-through of django cookbook (see van pelt franklin bookmarks)
# Chpt.1 Getting Started with Django 3.0
## Initial Setup
- create directory and venv
```
python3 -m venv .venv
```
- install django
```
pip install "Django~=3.0.0"
```
## File Structure Creation
- create the following dirs: 
    - `db_backups` directory for database dumps
    - `mockups` directory for website design files
    - `src` directory for your Django project.
- in `src`, start a new django project
```
django-admin.py startproject [project_name]
```
- executed command will create a directory called [project_name], with project files inside. This directory will contain a Python module, also called [project_name]. For clarity and convenience, rename the top-level directory as django-[project_name]. 
    - So now structure should be something like:
    ```
    app
    |
    └───src
        |
        └───django-db_form
            |
            └───db_form
    ```
- in the root ( django-[project_name] ) directory, create
    - A `media` directory for project uploads
    - A `static` directory for collected static files
    - A `locale` directory for project translations
    - An `externals` directory for external dependencies that are included in this project when you can't use the pip requirements

- the project directory should contain:
    - The `apps` directory where you will put all your in-house Django apps for the project. It is recommended that you have one app called core or utils for the projects' shared functionality.
    - The `settings` directory for your project settings (read about this in the Configuring settings for development, testing, staging, and production environments recipe).
    - The `site_static` directory for project-specific static files.
    - The `templates` directory for the project's HTML templates.
    - The `urls.py` file for the project's URL configuration.
    - The `wsgi.py` file for the project's web server configuration.

- In `site_static` directory, create the `site` directory as a namespace for site-specific static files
    - in `site`, create subdirectories for different categories of file:
        - `scss` for Sass files (optional)
        - `css` for the generated minified Cascading Style Sheets (CSS)
        - `img` for styling images, favicons, and logos
        - `js` for the project's JavaScriptdjango-admin.py startproject myproject
        - `vendor` for any third-party module combining all types of files, such as the TinyMCE rich-text editor

- entire structure for an app would look something like this
```
myproject_website/
├── commands/
├── db_backups/
├── mockups/
├── src/
│   └── django-myproject/
│       ├── externals/
│       │   ├── apps/
│       │   │   └── README.md
│       │   └── libs/
│       │       └── README.md
│       ├── locale/
│       ├── media/
│       ├── myproject/
│       │   ├── apps/
│       │   │   ├── core/
│       │   │   │   ├── __init__.py
│       │   │   │   └── versioning.py
│       │   │   └── __init__.py
│       │   ├── settings/
│       │   │   ├── __init__.py
│       │   │   ├── _base.py
│       │   │   ├── dev.py
│       │   │   ├── production.py
│       │   │   ├── sample_secrets.json
│       │   │   ├── secrets.json
│       │   │   ├── staging.py
│       │   │   └── test.py
│       │   ├── site_static/
│       │   │   └── site/
│       │   │  django-admin.py startproject myproject     ├── css/
│       │   │       │   └── style.css
│       │   │       ├── img/
│       │   │       │   ├── favicon-16x16.png
│       │   │       │   ├── favicon-32x32.png
│       │   │       │   └── favicon.ico
│       │   │       ├── js/
│       │   │       │   └── main.js
│       │   │       └── scss/
│       │   │           └── style.scss
│       │   ├── templates/
│       │   │   ├── base.html
│       │   │   └── index.html
│       │   ├── __init__.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       ├── requirements/
│       │   ├── _base.txt
│       │   ├── dev.txt
│       │   ├── production.txt
│       │   ├── staging.txt
│       │   └── test.txt
│       ├── static/
│       ├── LICENSE
│       └── manage.py
└── env/
```
- Can get a boilerplate project from `https://github.com/archatas/django-myproject.`
    - just need to global search and replace all references to `myproject` name
## Handling project dependencies with pip
- create a `requirements` directory with the following text files:

    - _base.txt for shared modules
    - dev.txt for the development environment
    - test.txt for the testing environment
    - staging.txt for the staging environment
    - production.txt for production

- add requirements that will be in all environments to `_base.txt`
- in other reqfiles, enter `-r _base.txt` as first line to incude the reqs from _base
    - add env-specific dependencies after the -r inclusion line

- good idea to narrow range of release versions for your dependencies so that nothing gets broken because of new versions with backwards incompatibility
## Configuring settings for development, testing, staging, and production environments
    In the [project_name] directory (not django-[project_name] ), create a settings Python module with the following files:

    - __init__.py makes the settings directory a Python module.
    - _base.py for shared settings
    - dev.py for development settings
    - test.py for testing settings
    - staging.py for staging settings
    - production.py for production settings

- copy the `settings.py` created by `startproject` command to be requirements/_base.py and delete the original file.

- Change the BASE_DIR in the settings/_base.py to point one level up. It should first look as follows:
```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```
- change so looks like
```
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
) ## ie. extra `os.path.dirname`
```
- if the settings of a particular environment are same as base, import them in that settings file
```
# myproject/settings/production.py
from ._base import *
```
- modify manage.py and [project]/wsgi.py to use a particular environment by default
```
os.environ.setdefault('DJANGO_SETTINGS_MODULE',  '[project].settings.production')
```
## Defining relative paths in the settings
- Django requires you to define different file paths in the settings, such as the root of your media, the root of your static files, the path to templates, and the path to translation files.
    - for each developer, these can differ depending on where the venv is created and what os is used
- to `_base.py` in settings, add/change:
```
    # settings/_base.py
    import os
    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    # ...
    TEMPLATES = [{
        # ...
        DIRS: [
        os.path.join(BASE_DIR, 'myproject', 'templates'),
        ],
        # ...
    }]
    # ...
    LOCALE_PATHS = [
        os.path.join(BASE_DIR, 'locale'),
    ]
    # ...
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'myproject', 'site_static'),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
## Handling sensitive settings
- want to read sensitive settings from the environment variables. To set this up:
1. Define `get_secret` function at beginning of _base.py settings file
```
    def get_secret(setting):
        """Get the secret variable or return explicit exception."""
        try:
            return os.environ[setting]
        except KeyError:
            error_msg = f'Set the {setting} environment variable'
            raise ImproperlyConfigured(error_msg)

```
2. Set the environment variables in the PyCharm configuration, remote server configuration consoles, in the env/bin/activate script, .bash_profile, or directly in the Terminal (e.g)
```
    export DJANGO_SECRET_KEY="change-this-to-50-characters-long-random-
    string"
    export DATABASE_NAME="myproject"
    export DATABASE_USER="myproject"
    export DATABASE_PASSWORD="change-this-to-database-password"
```

3. Use this function to retrieve envvar values, eg.
```
    SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': get_secret('DATABASE_NAME'),
            'USER': get_secret('DATABASE_USER'),
            'PASSWORD': get_secret('DATABASE_PASSWORD'),
            'HOST': 'db',
            'PORT': '5432',
        }
    }
```
## Including external dependencies in your project
- sometimes cant install dependencies with pip and need to include external ones
- in the `externals` directory, create the following structure:
```
    externals/
    ├── apps/
    │   ├── cms/
    │   ├── haystack/
    │   ├── storages/
    │   └── README.md
    └── libs/
        ├── boto/
        ├── requests/
        ├── twython/
        └── README.md
```
- put the external libraries and apps under the Python path so that they are recognized as if they were installed, adding the following to `settings/_base.py`:
```
    EXTERNAL_BASE = os.path.join(BASE_DIR, "externals")
    EXTERNAL_LIBS_PATH = os.path.join(EXTERNAL_BASE, "libs")
    EXTERNAL_APPS_PATH = os.path.join(EXTERNAL_BASE, "apps")
    sys.path = ["", EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path
```
## Setting up STATIC_URL dynamically
- If you set STATIC_URL to a static value, then each time you update a CSS file, a JavaScript file, or an image, you and your website visitors will need to clear the browser cache in order to see the changes. 
    - There is a trick to work around clearing the browser's cache: have the timestamp of the latest changes shown in STATIC_URL. Whenever the code is updated, the visitor's browser will force the loading of all new static files.

- in `.../apps/core`, create `versioning.py`:
```
    # versioning.py
    import subprocess
    from datetime import datetime


    def get_git_changeset_timestamp(absolute_path):
        repo_dir = absolute_path
        git_log = subprocess.Popen(
            "git log --pretty=format:%ct --quiet -1 HEAD",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            cwd=repo_dir,
            universal_newlines=True,
        )

        timestamp = git_log.communicate()[0]
        try:
            timestamp = datetime.utcfromtimestamp(int(timestamp))
        except ValueError:
            # Fallback to current timestamp
            return datetime.now().strftime('%Y%m%d%H%M%S')
        changeset_timestamp = timestamp.strftime('%Y%m%d%H%M%S')
        return changeset_timestamp
```
- Import the newly created get_git_changeset_timestamp() function in the settings and use it for the STATIC_URL path, as follows:
```
    # settings/_base.py
    from myproject.apps.core.versioning import get_git_changeset_timestamp
    # ...
    timestamp = get_git_changeset_timestamp(BASE_DIR)
    STATIC_URL = f'/static/{timestamp}/'
```
- This method works only if each of your environments contains the full Git repository of the project
    - In order to have the STATIC_URL with a dynamic fragment, you have to read the timestamp from a text file—for example, `[project]/settings/last-modified.txt` —that should be updated with each commit.
    - You can make your Git repository update last-modified.txt with a pre-commit hook. This is an executable bash script that should be called pre-commit and placed under `django-[project]/.git/hooks/`
## Creating the Git ignore file
    ```
    # .gitignore
    ### Python template
    # Byte-compiled / optimized / DLL files
    __pycache__/
    *.py[cod]
    *$py.class

    # Installer logs
    pip-log.txt
    pip-delete-this-directory.txt

    # Unit test / coverage reports
    htmlcov/
    .tox/
    .nox/
    .coverage
    .coverage.*
    .cache
    nosetests.xml
    coverage.xml
    *.cover
    .hypothesis/
    .pytest_cache/

    # Translations
    *.mo
    *.pot

    # Django stuff:
    *.log
    db.sqlite3

    # Sphinx documentation
    docs/_build/

    # IPython
    profile_default/
    ipython_config.py

    # Environments
    env/

    # Media and Static directories
    /media/
    !/media/.gitkeep

    /static/
    !/static/.gitkeep

    # Secrets
    secrets.json
    ```
- ignore the Python-compiled files, local settings, collected static files, and media directory with the uploaded files.
## Respecting the import order in Python files
- use the following order for imports in files
```
# System libraries
import os
import re
from datetime import datetime

# Third-party libraries
import boto
from PIL import Image

# Django modules
from django.db import models
from django.conf import settings

# Django apps
from cms.models import Page

# Current-app modules
from .models import NewsArticle
from . import app_settings
```
## Creating an app configuration
- django projects consist of multiple modules called applications that combine different modular functionalities
- Django framework has an application registry, where all apps and models are collected and later used for configuration and introspection. 
- metainformation about apps can be saved in the AppConfig instance for each app.
- to create app:
```
cd [project]/apps/
django-admin.py startapp [app]
```
- In the new [app] directory:
    - add a view
    ```
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Form Landing Page.")
    ```
    - create `urls.py` and add:
    ```
    from django.urls import path

    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```
    - add a model
    ```
    class Form(models.Model):
        study_name = models.CharField(max_length=200)
        primary_investigator = models.CharField(max_length=200)
        submit_date = models.DateTimeField('date published')
    ```
    - register model for admin interface use:
    ```
    ## admin.py
    from .models import Form

    admin.site.register(Form)
    ```
    - in main directory `_base.py` setting file, register the new app:
        - add `"[myproject].[apps].[app]"` to `INSTALLED_APPS` list

    - make migration and migrate
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
## Defining overwritable app settings
- you can define settings for your app that can then be overwritten in your project's settings file. 
    - This is especially useful for reusable apps that you can customize by adding a configuration.
1. Define your app settings using the `getattr()` pattern in` models.py` if you just have one or two settings, or in the `app_settings.py` file if the settings are extensive and you want to organize them better
    ```
        # myproject/apps/magazine/app_settings.py
        from django.conf import settings
        from django.utils.translation import gettext_lazy as _

        # Example:
        SETTING_1 = getattr(settings, "MAGAZINE_SETTING_1", "default value")

        MEANING_OF_LIFE = getattr(settings, "MAGAZINE_MEANING_OF_LIFE", 42)

        ARTICLE_THEME_CHOICES = getattr(
            settings,
            "MAGAZINE_ARTICLE_THEME_CHOICES",
            [
                ('futurism', _("Futurism")),
                ('nostalgia', _("Nostalgia")),
                ('sustainability', _("Sustainability")),
                ('wonder', _("Wonder")),
            ]
        )

    ```
2. `models.py` will then contain a model/models
    ```
        # myproject/apps/magazine/models.py
        from django.db import models
        from django.utils.translation import gettext_lazy as _


        class NewsArticle(models.Model):
            created_at = models.DateTimeField(_("Created at"),  
            auto_now_add=True)
            title = models.CharField(_("Title"), max_length=255)
            body = models.TextField(_("Body"))
            theme = models.CharField(_("Theme"), max_length=20)

            class Meta:
                verbose_name = _("News Article")
                verbose_name_plural = _("News Articles")

            def __str__(self):
                return self.title
    ```
3. import and use the settings from app_settings.py in `admin.py` 
4. to overwrite the a given setting for a given project, add the setting name ( part in quotes, second arg of `getattr()` ) and new value in the project settings file:
    ```
        # myproject/settings/_base.py
        from django.utils.translation import gettext_lazy as _

        MAGAZINE_ARTICLE_THEME_CHOICES = [
            ('futurism', _("Futurism")),
            ('nostalgia', _("Nostalgia")),
            ('sustainability', _("Sustainability")),
            ('wonder', _("Wonder")),
            ('positivity', _("Positivity")),
            ('solutions', _("Solutions")),
            ('science', _("Science")),
        ]
    ```
## Working with Docker containers for Django, Gunicorn, Nginx, and PostgreSQL
- can use Docker to ensure that all environments and all developers will have all the same requirements installed.
- get boilerplate for django/psql/nginx/gunicorn setup
    ```
    git clone https://github.com/archatas/django_docker.git
    ```
- copy the file `build_dev_example.sh` to be `build_dev.sh` and edit values as indicated
- bring up services with `sudo ./build_dev.sh`
- inspect logs of containers with 
    ```
        docker-compose logs nginx
        docker-compose logs gunicorn
        docker-compose logs db
    ```
# Chpt.2 Models and Database Structure
## Using Model Mixins
- in python, a mixin class can be viewed as an interface with implemented features
- when a model extends a mixin, it implements the interface and includes all of its fields, attributes, properties, and methods.
- mixins in Django models can be used when you want to reuse the generic functionalities in different models multiple times.
- good place to keep your mixins in in the [myproject].[apps].[core] app
- using mixings:
    - in `models.py` of app that you want to use mixins in:
        ```
            # myproject/apps/ideas/models.py
            from django.db import models
            from django.urls import reverse
            from django.utils.translation import gettext_lazy as _

            from myproject.apps.core.models import (
                CreationModificationDateBase,
                MetaTagsBase,
                UrlBase,
            )<--- importing the mixins here

            class Idea(CreationModificationDateBase, MetaTagsBase, UrlBase):
                title = models.CharField(
                    _("Title"),
                    max_length=200,
                )
                content = models.TextField(
                    _("Content"),
                )
                # other fields…

                class Meta:
                    verbose_name = _("Idea")
                    verbose_name_plural = _("Ideas")

                def __str__(self):
                    return self.title

                def get_url_path(self):
                    return reverse("idea_details", kwargs={
                        "idea_id": str(self.pk),
                    })
        ```
        - `Idea` class inherits all the fields, props, methods of the abstract class mixins
        - all of the fields of these abstract classes are saved in the same database table as the fields of the extending model. 
        - Django model base classes follow normal python inheritance (if a child class inherits from several base classes that all implement the same-named function, calling that function in the child will result in only the first-passed-in base class's function being called), but Django framework does some magic with metaclasses that calls the save() and delete() methods from each of the base classes.
            - this means you can confidently do pre-save, post-save, pre-delete, and post-delete manipulations for specific fields defined specifically in the mixin by overwriting the save() and delete() methods.
## Creating a model mixin with URL-related methods
- For every model that has its own distinct detail page, it is good practice to define the `get_absolute_url()` method
    - this method is ambiguous however, as it returns the URL path and not the full URL
- we want to create a model mixin that provides simplified support for model-specific URLs that will allow:
    - Allow you to define either the URL path or the full URL in your model
    - Generate the other URL automatically, based on the one that you defined
    - Define the get_absolute_url() method behind the scenes

Steps:
1. Create `models.py` in the `core` app ( under `apps` dir ) 
2. add code:
    ```
        # myproject/apps/core/models.py
        from urllib.parse import urlparse, urlunparse
        from django.conf import settings
        from django.db import models

        class UrlBase(models.Model):
            """
            A replacement for get_absolute_url()
            Models extending this mixin should have either get_url or 
            get_url_path implemented.
            """
            class Meta:
                abstract = True

            def get_url(self):
                if hasattr(self.get_url_path, "dont_recurse"):
                    raise NotImplementedError
                try:
                    path = self.get_url_path()
                except NotImplementedError:
                    raise
                return settings.WEBSITE_URL + path
            get_url.dont_recurse = True

            def get_url_path(self):
                if hasattr(self.get_url, "dont_recurse"):
                    raise NotImplementedError
                try:
                    url = self.get_url()
                except NotImplementedError:
                    raise
                bits = urlparse(url)
                return urlunparse(("", "") + bits[2:])
            get_url_path.dont_recurse = True

            def get_absolute_url(self):
                return self.get_url()
    ```
3. Add the WEBSITE_URL setting without a trailing slash to the dev, test, staging, and production settings. For example, for the development environment this will be as follows:
    ```
        # myproject/settings/dev.py
        from ._base import *

        DEBUG = True
        WEBSITE_URL = "http://127.0.0.1:8000"  # without trailing slash
    ```
4. To use the mixin in your app, import the mixin from the core app, inherit the mixin in your model class, and define the get_url_path() method, as follows:
    ```
        # myproject/apps/ideas/models.py
        from django.db import models
        from django.urls import reverse
        from django.utils.translation import gettext_lazy as _

        from myproject.apps.core.models import UrlBase

        class Idea(UrlBase):
            # fields, attributes, properties and methods…

            def get_url_path(self):
                return reverse("idea_details", kwargs={
                    "idea_id": str(self.pk),
                })
    ```
- The `get_url()` and `get_url_path()` methods are expected to be overwritten in the extended model class, for example, Idea. You can define `get_url()`, `and get_url_path()` will strip it to the path. Alternatively, you can define `get_url_path()`, and `get_url()` will prepend the website URL to the beginning of the path.
    - rule of thumb is to rewrite the `get_url_path()` method
    - In the templates, use get_url_path() when you need a link to an object on the same website
        ```
        <a href="{{ idea.get_url_path }}">{{ idea.title }}</a>
        ```
    - Use get_url() for links in external communication, such as in emails, RSS feeds, or APIs  
        ```
        <a href="{{ idea.get_url }}">{{ idea.title }}</a>
        ```
- should not use incremental primary keys in the URLs, because it is not safe to expose them to the end user
    - the total amount of items would be visible, and it would be too easy to navigate through different items by just changing the URL pattern
    - instead, define a "slug" field
        ```
            class Idea(UrlBase):
            slug = models.SlugField(_("Slug for URLs"), max_length=50)
        ```
## Creating a model mixin to handle creation and modification dates
- mixin for this ensures that timestamps are the same across all models
    ```
        # myproject/apps/core/models.py
        from django.db import models
        from django.utils.translation import gettext_lazy as _


        class CreationModificationDateBase(models.Model):
            """
            Abstract base class with a creation and modification date and time
            """

            created = models.DateTimeField(
                _("Creation Date and Time"),
                auto_now_add=True,
            )

            modified = models.DateTimeField(
                _("Modification Date and Time"),
                auto_now=True,
            )

            class Meta:
                abstract = True
    ```
- use the mixin to extend model classes
    ```
        # myproject/apps/ideas/models.py
        from django.db import models

        from myproject.apps.core.models import CreationModificationDateBase

        class Idea(CreationModificationDateBase):
            # other fields, attributes, properties, and methods…
    ```
- with `auto_now_add` and `auto_now` attributes, the timestamps will be saved automatically when saving a model instance.  
- fields will automatically get the `editable=False` attribute, and thus will be hidden in administration forms.
## Creating a model mixin to take care of meta tags
- appropriate meta tags aid SEO
- create a directory structure, `templates/utils/includes/`, under the `core` package, and inside of that, create a `meta.html` file to store the basic meta tag markup.
- To create the model mixin:
1. Make sure "myproject.apps.core" is in INSTALLED_APP (settings)
2. add tag html to `meta.html`
    ```
        {# templates/core/includes/meta_field.html #}
        <meta name="{{ name }}" content="{{ content }}" />
    ```
3. Build mixin in `core/models.py`
    ```
        # myproject/apps/core/models.py
        from django.conf import settings
        from django.db import models
        from django.utils.translation import gettext_lazy as _
        from django.utils.safestring import mark_safe
        from django.template.loader import render_to_string


        class MetaTagsBase(models.Model):
            """
            Abstract base class for generating meta tags
            """
            meta_keywords = models.CharField(
                _("Keywords"),
                max_length=255,
                blank=True,
                help_text=_("Separate keywords with commas."),
            )
            meta_description = models.CharField(
                _("Description"),
                max_length=255,
                blank=True,
            )
            meta_author = models.CharField(
                _("Author"),
                max_length=255,
                blank=True,
            )
            meta_copyright = models.CharField(
                _("Copyright"),
                max_length=255,
                blank=True,
            )

            class Meta:
                abstract = True

            def get_meta_field(self, name, content):
                tag = ""
                if name and content:
                    tag = render_to_string("core/includes/meta_field.html", 
                    {
                        "name": name,
                        "content": content,
                    })
                return mark_safe(tag)

            def get_meta_keywords(self):
                return self.get_meta_field("keywords", self.meta_keywords)

            def get_meta_description(self):
                return self.get_meta_field("description", 
                self.meta_description)

            def get_meta_author(self):
                return self.get_meta_field("author", self.meta_author)

            def get_meta_copyright(self):
                return self.get_meta_field("copyright", 
                self.meta_copyright)

            def get_meta_tags(self):
                return mark_safe("\n".join((
                    self.get_meta_keywords(),
                    self.get_meta_description(),
                    self.get_meta_author(),
                    self.get_meta_copyright(),
                )))
    ```
- if used with model such as Idea, can put the following blocks in <head> section of page template to render all meta tags at once
    ```
        {% block meta_tags %}
        {{ block.super }}
        {{ idea.get_meta_tags }}
        {% endblock %}
    ```
## Creating a model mixin to handle generic relations
- Generic relations: django mechanism to relate a model to an instance of any other model 
    - For each generic relation, the content type of the related model as well as the ID of the instance of that model is saved.
- Must have `contenttypes` app installed in `settings.py` INSTALLED_APPS list.
- in core app's `models.py`:
    ```
        # myproject/apps/core/models.py
        from django.db import models
        from django.utils.translation import gettext_lazy as _
        from django.contrib.contenttypes.models import ContentType
        from django.contrib.contenttypes.fields import GenericForeignKey
        from django.core.exceptions import FieldError


        def object_relation_base_factory(
                prefix=None,
                prefix_verbose=None,
                add_related_name=False,
                limit_content_type_choices_to=None,
                is_required=False):
            """
            Returns a mixin class for generic foreign keys using
            "Content type - object ID" with dynamic field names.
            This function is just a class generator.

            Parameters:
            prefix:           a prefix, which is added in front of
                            the fields
            prefix_verbose:   a verbose name of the prefix, used to
                            generate a title for the field column
                            of the content object in the Admin
            add_related_name: a boolean value indicating, that a
                            related name for the generated content
                            type foreign key should be added. This
                            value should be true, if you use more
                            than one ObjectRelationBase in your
                            model.

            The model fields are created using this naming scheme:
                <<prefix>>_content_type
                <<prefix>>_object_id
                <<prefix>>_content_object
            """
            p = ""
            if prefix:
                p = f"{prefix}_"

            prefix_verbose = prefix_verbose or _("Related object")
            limit_content_type_choices_to = limit_content_type_choices_to 
            or {}

            content_type_field = f"{p}content_type"
            object_id_field = f"{p}object_id"
            content_object_field = f"{p}content_object"

            class TheClass(models.Model):
                class Meta:
                    abstract = True

            if add_related_name:
                if not prefix:
                    raise FieldError("if add_related_name is set to "
                                    "True, a prefix must be given")
                related_name = prefix
            else:
                related_name = None

            optional = not is_required

            ct_verbose_name = _(f"{prefix_verbose}'s type (model)")

            content_type = models.ForeignKey(
                ContentType,
                verbose_name=ct_verbose_name,
                related_name=related_name,
                blank=optional,
                null=optional,
                help_text=_("Please select the type (model) "
                            "for the relation, you want to build."),
                limit_choices_to=limit_content_type_choices_to,
                on_delete=models.CASCADE)

            fk_verbose_name = prefix_verbose

            object_id = models.CharField(
                fk_verbose_name,
                blank=optional,
                null=False,
                help_text=_("Please enter the ID of the related object."),
                max_length=255,
                default="")  # for migrations

            content_object = GenericForeignKey(
                ct_field=content_type_field,
                fk_field=object_id_field)

            TheClass.add_to_class(content_type_field, content_type)
            TheClass.add_to_class(object_id_field, object_id)
            TheClass.add_to_class(content_object_field, content_object)

            return TheClass
    ```
    - This mixin is then used like in this example:
        ```
            # myproject/apps/ideas/models.py
            from django.db import models
            from django.utils.translation import gettext_lazy as _

            from myproject.apps.core.models import (
                object_relation_base_factory as generic_relation,
            )


            FavoriteObjectBase = generic_relation(
                is_required=True,
            )


            OwnerBase = generic_relation(
                prefix="owner",
                prefix_verbose=_("Owner"),
                is_required=True,
                add_related_name=True,
                limit_content_type_choices_to={
                    "model__in": (
                        "user",
                        "group",
                    )
                }
            )


            class Like(FavoriteObjectBase, OwnerBase):
                class Meta:
                    verbose_name = _("Like")
                    verbose_name_plural = _("Likes")

                def __str__(self):
                    return _("{owner} likes {object}").format(
                        owner=self.owner_content_object,
                        object=self.content_object
                    )
        ```
- `object_relation_base_factory` isn't a mixin itself, rather is a function generating a mixin
    - it is a dynamically created mixin that adds the `content_type` and `object_id` fields and the `content_object` generic foreign key that points to the related instance.
## Avoiding circular dependencies
- should avoid python modules that import from eachother
1. For foreign keys and many-to-many relationships with models from other apps, use the "<app_label>.<model>" declaration instead of importing the model. 
    - In Django this works with ForeignKey, OneToOneField, and ManyToManyField
    ```
    # myproject/apps/ideas/models.py
    from django.db import models
    from django.conf import settings
    from django.utils.translation import gettext_lazy as _

    class Idea(models.Model):
        author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            verbose_name=_("Author"),
            on_delete=models.SET_NULL,
            blank=True,
            null=True,
        )
        category = models.ForeignKey(
            "categories.Category",
            verbose_name=_("Category"),
            blank=True,
            null=True,
            on_delete=models.SET_NULL,
        )
        # other fields, attributes, properties and methods…
    ```
2. If you need to access a model from another app in a method, import that model inside the method instead of at the module level
    ```
        # myproject/apps/categories/models.py
        from django.db import models
        from django.utils.translation import gettext_lazy as _

        class Category(models.Model):
            # fields, attributes, properties, and methods…

            def get_ideas_without_this_category(self):
                from myproject.apps.ideas.models import Idea
                return Idea.objects.exclude(category=self)
    ```
3. If you use model inheritance, for example, for model mixins, keep the base classes in a separate app and place them before other apps that would use them in INSTALLED_APPS
    - eg. could keep base classes in `core` app and then order like:
        ```
            INSTALLED_APPS = [
            # contributed
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            # third-party
            # ...
            # local
            "myproject.apps.core",<-----
            "myproject.apps.categories",
            "myproject.apps.ideas",
]
        ```
## Adding database constraints
- Set the database constraints in the `Meta` class of a model
    - eg.
        ```
            ...
            class Meta:
                verbose_name = _("Idea")
                verbose_name_plural = _("Ideas")
                constraints = [
                    models.UniqueConstraint(
                        fields=["title"],
                        condition=~models.Q(author=None),
                        name="unique_titles_for_each_author",
                    ),
                    models.CheckConstraint(
                        check=models.Q(
                            title__iregex=r"^\S.*\S$"
                            # starts with non-whitespace,
                            # ends with non-whitespace,
                            # anything in the middle
                        ),
                        name="title_has_no_leading_and_trailing_whitespaces",
                    )
                ]
        ```
    - `UniqueConstraint` ensured via `negated lookup`: ~models.Q(author=None). 
        - Note that in Django, the `~` operator for lookups is equivalent to the exclude() method of a QuerySet
    - Database constraints don't affect form validation. 
        - will just raise `django.db.utils.IntegrityError `if any data doesn't pass its conditions when saving entries to the database.
        - If you want to have data validated at the forms, you have to implement the validation in addition yourself, for example, in the clean() method of the model.
            - eg.
                ```
                    ...
                    def clean(self):
                        import re
                        if self.author and Idea.objects.exclude(pk=self.pk).filter(
                            author=self.author,
                            title=self.title,
                        ).exists():
                            raise ValidationError(
                                _("Each idea of the same user should have a unique title.")
                            )
                        if not re.match(r"^\S.*\S$", self.title):
                            raise ValidationError(
                                _("The title cannot start or end with a whitespace.")
                            )
                ```
## Using Migrations
- create database tables for given app
    ```
    python manage.py makemigrations ideas
    ```
- execute migrations for specific app (to run for all apps, leave off app designation at end)
    ```
    python manage.py migrate ideas
    ```
- to add to or change data in the existing schema in bulk, you use a data migration instead of a schema migration
    ```
    python manage.py makemigrations --name=populate_subtitle > --empty ideas
    ```
    - `--empty` parameter tells Django to create a skeleton data migration, which you have to modify to perform the necessary data manipulation before applying it
- you can migrate back and forth by specifying the number of the migration to which we want to migrate
    ```
    python manage.py migrate ideas 0002
    ```
    - and you can migrate all the way back to starting state with `python manage.py migrate [app] zero`

## Changing a foreign key to the many-to-many field
- using schema and data migrations, can change a many-to-one relation to a many-to-many relation, while preserving the already existing data
- a many-to-one relationship is defined with `models.ForeignKey()`, whereas a many-to-many relationship uses `models.ManyToManyField()`
- to make the change
    - add the ManyToManyField() relationship in the existing model
    - run `makemigration` and `migrate` commands
    - Create a data migration to copy the categories from the foreign key to the many-to-many field
        ```
            python manage.py makemigrations --empty \
            > --name=migration_name [app]
        ```
    - open the new migration file and define the forward migration instructions, eg.
        ```
            # myproject/apps/ideas/migrations/0003_copy_categories.py
            from django.db import migrations


            def copy_categories(apps, schema_editor):<-------add this
                Idea = apps.get_model("ideas", "Idea")
                for idea in Idea.objects.all():
                    if idea.category:
                        idea.categories.add(idea.category)


            class Migration(migrations.Migration):

                dependencies = [
                    ('ideas', '0002_idea_categories'),
                ]

                operations = [
                    migrations.RunPython(copy_categories),<-----add this
                ]
        ```
    - run the new migration
    - delete the foreignKey relationship in the model
    - makemigration/migrate one more time
# Chpt.3 Forms and Views
## Saving the author of a model instance
- By default, forms that are used by views accept the GET or POST data, files, initial data, and other parameters; however, they do not inherently have access to the HttpRequest object. 
    - In some cases, it is useful to additionally pass HttpRequest to the form, especially when you want to filter out the choices of form fields based on other request data or handle saving something such as the current user or IP in the form.
- Can have a form where, for added or changed ideas, the current user is saved as an author
    1. Create an form object
        ```
        # myprojects/apps/ideas/forms.py
        from django import forms
        from .models import Idea

        class IdeaForm(forms.ModelForm):
            class Meta:
                model = Idea
                exclude = ["author"]

            def __init__(self, request, *args, **kwargs):
                self.request = request
                super().__init__(*args, **kwargs)

            def save(self, commit=True):
                instance = super().save(commit=False)
                instance.author = self.request.user
                if commit:
                    instance.save()
                    self.save_m2m()
                return instance
        ```
    2. Create a view that allow addition/change of Ideas
        ```
        # myproject/apps/ideas/views.py
        from django.contrib.auth.decorators import login_required
        from django.shortcuts import render, redirect, get_object_or_404

        from .forms import IdeaForm
        from .models import Idea


        @login_required
        def add_or_change_idea(request, pk=None):
            idea = None
            if pk:
                idea = get_object_or_404(Idea, pk=pk)

            if request.method == "POST":
                form = IdeaForm(request, data=request.POST, 
                files=request.FILES, instance=idea)
            
                if form.is_valid():
                    idea = form.save()
                    return redirect("ideas:idea_detail", pk=idea.pk)
            else:
                form = IdeaForm(request, instance=idea)

            context = {"idea": idea, "form": form}
            return render(request, "ideas/idea_form.html", context)
        ```
    - How the form works:
        - At first, we exclude the author field from the form because we want to handle it programatically. 
        - We overwrite the __init__() method to accept HttpRequest as the first parameter and store it in the form.
        - The commit parameter tells the model form to save the instance immediately or otherwise to create and populate the instance, but not save it yet. 
            - In our case, we get the instance without saving it, then assign the author from the current user. 
        - Finally, we save the instance if commit is True. We will call the dynamically added save_m2m() method of the form to save many-to-many relations, for example, categories.

## Uploading images
- for images with different versions (eg. sizes ) need the `Pillow` and `django-imagekit` libraries.
    - add `imagekit` to INSTALLED_APPS in settings
1. Add picture field and image specs to model
    ```
        # myproject/apps/ideas/models.py
        import contextlib
        import os

        from imagekit.models import ImageSpecField
        from pilkit.processors import ResizeToFill

        from django.db import models
        from django.utils.translation import gettext_lazy as _
        from django.utils.timezone import now as timezone_now

        from myproject.apps.core.models import (CreationModificationDateBase, UrlBase)


        def upload_to(instance, filename):
            now = timezone_now()
            base, extension = os.path.splitext(filename)
            extension = extension.lower()
            return f"ideas/{now:%Y/%m}/{instance.pk}{extension}"


        class Idea(CreationModificationDateBase, UrlBase):
            # attributes and fields…
            picture = models.ImageField(
                _("Picture"), upload_to=upload_to
            )
            picture_social = ImageSpecField(
                source="picture",
                processors=[ResizeToFill(1024, 512)],
                format="JPEG",
                options={"quality": 100},
            )
            picture_large = ImageSpecField(
                source="picture", 
                processors=[ResizeToFill(800, 400)], 
                format="PNG"
            )
            picture_thumbnail = ImageSpecField(
                source="picture", 
                processors=[ResizeToFill(728, 250)], 
                format="PNG"
            )
            # other fields, properties, and  methods…

            def delete(self, *args, **kwargs):
                from django.core.files.storage import default_storage
                if self.picture:
                    with contextlib.suppress(FileNotFoundError):
                        default_storage.delete(
                            self.picture_social.path
                        )
                        default_storage.delete(
                            self.picture_large.path
                        )
                        default_storage.delete(
                            self.picture_thumbnail.path
                        )
                    self.picture.delete()
                super().delete(*args, **kwargs)
    ```
2. Create a model form for your model in `forms.py`
3. In the view for adding or changing ideas, make sure to post request.FILES beside request.POST to the form
    ```
    # myproject/apps/ideas/views.py
    from django.contrib.auth.decorators import login_required
    from django.shortcuts import (render, redirect, get_object_or_404)
    from django.conf import settings

    from .forms import IdeaForm
    from .models import Idea


    @login_required
    def add_or_change_idea(request, pk=None):
        idea = None
        if pk:
            idea = get_object_or_404(Idea, pk=pk)
        if request.method == "POST":
            form = IdeaForm(
                request, 
                data=request.POST, 
                files=request.FILES, 
                instance=idea,
            )
            
            if form.is_valid():
                idea = form.save()
                return redirect("ideas:idea_detail", pk=idea.pk)
        else:
            form = IdeaForm(request, instance=idea)

        context = {"idea": idea, "form": form}
        return render(request, "ideas/idea_form.html", context)
    ```
4. In the template, make sure to have encoding type set to "multipart/form-data"
    ```
    <form action="{{ request.path }}" method="post" enctype="multipart/form-data">{% csrf_token %}
    {{ form.as_p }}
    <button type="submit">{% trans "Save" %}</button>
    </form>
    ```
- Django model forms are created dynamically from models.
    - they provide the specified fields from the model so you don't need to redefine them manually
    - When we save the form, the form knows how to save each field in the database, as well as how to upload the files and save them in the media directory
## Creating a form layout with custom templates
1. In `settings.py`, ensure that the template system will be able to find customized templates by:
    - adding "django.forms" to INSTALLED_APPS 
    - including the APP_DIRS flag as True at the templates configuration, 
    - and using the "TemplatesSetting" form renderer, ie
        ```
        ...
        FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
        ...
        ```
2. Create template in `widgets` directory under `core` app

## Creating a form layout with django-crispy-forms
- `django-crispy-forms` Django app allows you to build, customize, and reuse forms using Uni-Form, Bootstrap 3, Bootstrap 4, or Foundation
- Setup:
    1. Integrate bootstrap CSS/JS files into `base.html`
        - can use the CDN and simply add the appropriate `<script> ` tags to .html
        - see https://getbootstrap.com/docs/4.3/getting-started/introduction/ 
    2. pip install django-crispy-forms
    3. Add `crispy-forms` to INSTALLED_APPS
    4. set `CRISPY_TEMPLATE_PACK` value in settings.py ( eg. to `bootstap4` )
- use
    1. Add `from crispy_forms import bootstrap, helper, layout` to your `forms.py`
    2. Create form class with things like:
        ```
        class IdeaForm(forms.ModelForm):
            class Meta:
                model = Idea
                exclude = ["author"]

            def __init__(self, request, *args, **kwargs):
                self.request = request
                super().__init__(*args, **kwargs)

                self.fields["categories"].widget = 
                forms.CheckboxSelectMultiple()

                title_field = layout.Field(
                    "title", css_class="input-block-level"
                )
                content_field = layout.Field(
                    "content", css_class="input-block-level", rows="3"
                )
                main_fieldset = layout.Fieldset(
                    _("Main data"), title_field, content_field
                )

                picture_field = layout.Field(
                    "picture", css_class="input-block-level"
                )
                format_html = layout.HTML(
                    """{% include "ideas/includes
                        /picture_guidelines.html" %}"""
                )

                picture_fieldset = layout.Fieldset(
                    _("Picture"),
                    picture_field,
                    format_html,
                    title=_("Image upload"),
                    css_id="picture_fieldset",
                )

                categories_field = layout.Field(
                    "categories", css_class="input-block-level"
                )
                categories_fieldset = layout.Fieldset(
                    _("Categories"), categories_field,
                    css_id="categories_fieldset"
                )

                submit_button = layout.Submit("save", _("Save"))
                actions = bootstrap.FormActions(submit_button)

                self.helper = helper.FormHelper()
                self.helper.form_action = self.request.path
                self.helper.form_method = "POST"
                self.helper.layout = layout.Layout(
                    main_fieldset,
                    picture_fieldset,
                    categories_fieldset,
                    actions,
                )
        ```
## Working with formsets
- formset: sets of forms of the same type that allow us to create or change multiple instances at once.
    -  can be enriched with JavaScript, which allows us to add them to a page dynamically.
    - eg. if you want to use the form below multiple times in same view
        ```
            class UserForm(forms.ModelForm):
                class Meta:
                    model = User
                    fields = ["username", "email"]
        ```
        - in `views.py`
            ```
            from django.forms.formsets import formset_factory
            Uforms = formset_factory(UserForm, extra = 4)  #extra used to define how many empty forms will display

            def submit(request):
                if request.POST:
                    #code to manage post request
                    # validation to formset you can follow django docs
                else:
                    address_formSet = Uforms(instance=UserForm())
            ```

## Filtering object lists
- EX: creating is a list view of ideas that can be filtered by author, category, or rating.
    1. in `forms.py`, create `IdeaFilterForm` containing the filter facets, using the `queryset` to produce the options for selection
        ```
        class IdeaFilterForm(forms.Form):
            author = forms.ModelChoiceField(
                label=_("Author"),
                required=False,
                queryset=User.objects.annotate(
                    idea_count=models.Count("authored_ideas")
                ).filter(idea_count__gt=0),
            )
            ...
        ```
    2. Create view to list filtered objects
        ```
        def idea_list(request):
            qs = Idea.objects.order_by("title")
            form = IdeaFilterForm(data=request.GET)

            facets = {
                "selected": {},
                "categories": {
                    "authors": form.fields["author"].queryset,
                    "categories": form.fields["category"].queryset,
                    "ratings": RATING_CHOICES,
                },
            }

            if form.is_valid():
                filters = (
                    # query parameter, filter parameter
                    ("author", "author"),
                    ("category", "categories"),
                    ("rating", "rating"),
                )
                qs = filter_facets(facets, qs, form, filters)

            context = {"form": form, "facets": facets, "object_list": qs}
            return render(request, "ideas/idea_list.html", context)
        ```
    3. Make `filter_facets` helper function in same file
        ```
        def filter_facets(facets, qs, form, filters):
            for query_param, filter_param in filters:
                value = form.cleaned_data[query_param]
                if value:
                    selected_value = value
                    if query_param == "rating":
                        rating = int(value)
                        selected_value = (rating, 
                        dict(RATING_CHOICES)[rating])
                    facets["selected"][query_param] = selected_value
                    filter_args = {filter_param: value}
                    qs = qs.filter(**filter_args).distinct()
            return qs
        ```
    4. Create `idea_list.html` template 
        ```
            {# ideas/idea_list.html #}
            {% extends "base.html" %}
            {% load i18n utility_tags %}

            {% block sidebar %}
                {% include "ideas/includes/filters.html" %}
            {% endblock %}

            {% block main %}
                <h1>{% trans "Ideas" %}</h1>
                {% if object_list %}
                    {% for idea in object_list %}
                        <a href="{{ idea.get_url_path }}" class="d-block my-3">
                            <div class="card">
                            <img src="{{ idea.picture_thumbnail.url }}" 
                            alt="" />
                            <div class="card-body">
                                <p class="card-text">{{ idea.translated_title 
                                }}</p>
                            </div>
                            </div>
                        </a>
                    {% endfor %}
                {% else %}
                    <p>{% trans "There are no ideas yet." %}</p>
                {% endif %}
                <a href="{% url 'ideas:add_idea' %}" class="btn btn-primary">
                {% trans "Add idea" %}</a>
            {% endblock %}
        ```
    5. Create the template for the filters, using the `{% modify_query %}` template tag
        ```
        {# ideas/includes/filters.html #}
        {% load i18n utility_tags %}
        <div class="filters panel-group" id="accordion">
            {% with title=_('Author') selected=facets.selected.author %}
                <div class="panel panel-default my-3">
                    {% include "misc/includes/filter_heading.html" with 
                    title=title %}
                    <div id="collapse-{{ title|slugify }}"
                        class="panel-collapse{% if not selected %} 
                        collapse{% endif %}">
                        <div class="panel-body"><div class="list-group">
                            {% include "misc/includes/filter_all.html" with 
                            param="author" %}
                            {% for cat in facets.categories.authors %}
                                <a class="list-group-item
                                {% if selected == cat %}
                                active{% endif %}"
                                href="{% modify_query "page" 
                                    author=cat.pk %}">
                                    {{ cat }}</a>
                            {% endfor %}
                        </div></div>
                    </div>
                </div>
            {% endwith %}
            {% with title=_('Category') selected=facets.selected
            .category %}
                <div class="panel panel-default my-3">
                    {% include "misc/includes/filter_heading.html" with 
                    title=title %}
                    <div id="collapse-{{ title|slugify }}"
                        class="panel-collapse{% if not selected %} 
                        collapse{% endif %}">
                        <div class="panel-body"><div class="list-group">
                            {% include "misc/includes/filter_all.html" with 
                            param="category" %}
                            {% for cat in facets.categories.categories %}
                                <a class="list-group-item
                                {% if selected == cat %}
                                active{% endif %}"
                                href="{% modify_query "page" 
                                    category=cat.pk %}">
                                    {{ cat }}</a>
                            {% endfor %}
                        </div></div>
                    </div>
                </div>
            {% endwith %}
            {% with title=_('Rating') selected=facets.selected.rating %}
                <div class="panel panel-default my-3">
                    {% include "misc/includes/filter_heading.html" with 
                    title=title %}
                    <div id="collapse-{{ title|slugify }}"
                        class="panel-collapse{% if not selected %} 
                        collapse{% endif %}">
                        <div class="panel-body"><div class="list-group">
                            {% include "misc/includes/filter_all.html" with 
                            param="rating" %}
                            {% for r_val, r_display in 
                            facets.categories.ratings %}
                                <a class="list-group-item
                                {% if selected.0 == r_val %}
                                active{% endif %}"
                                href="{% modify_query "page" 
                                    rating=r_val %}">
                                    {{ r_display }}</a>
                            {% endfor %}
                        </div></div>
                    </div>
                </div>
            {% endwith %}
        </div>
        ```
    6. create and include templates with the common parts of filters
        - `misc/includes/filter_heading.html` - filter heading
            ```
            {# misc/includes/filter_heading.html #}
            {% load i18n %}
            <div class="panel-heading">
                <h6 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion"
                    href="#collapse-{{ title|slugify }}">
                        {% blocktrans trimmed %}
                            Filter by {{ title }}
                        {% endblocktrans %}
                    </a>
                </h6>
            </div
            ```
        - `misc/includes/filter_all.html` - link to reset filter
            ```
            {# misc/includes/filter_all.html #}
            {% load i18n utility_tags %}
            <a class="list-group-item {% if not selected %}active{% endif %}"
            href="{% modify_query "page" param %}">
                {% trans "All" %}
            </a>
            ```
    7. Add ideasList to app's `urls.py`
        ```
        # myproject/apps/ideas/urls.py
        from django.urls import path

        from .views import idea_list

        urlpatterns = [
            path("", idea_list, name="idea_list"),
            # other paths…
        ]
        ```
## Managing paginated lists
- in `views.py`:
    ```
        from django.core.paginator import (EmptyPage, PageNotAnInteger, Paginator)
        ...
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get("page")
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            # If page is not an integer, show first page.
            page = paginator.page(1)
        except EmptyPage:
            # If page is out of range, show last existing page.
            page = paginator.page(paginator.num_pages)

        context = {
            "form": form,
            "facets": facets, 
            "object_list": page,
        }
        return render(request, "ideas/idea_list.html", context)
    ```
- add something like below in template:
    ```
    {% include "misc/includes/pagination.html" %}
    ```
- create `pagination.html` template
    ```
    {# misc/includes/pagination.html #}
    {% load i18n utility_tags %}
    {% if object_list.has_other_pages %}
        <nav aria-label="{% trans 'Page navigation' %}">

            <ul class="pagination">
                {% if object_list.has_previous %}
                    <li class="page-item"><a class="page-link" href="{% 
            modify_query page=object_list.previous_page_number %}">
                        {% trans "Previous" %}</a></li>
                {% else %}
                    <li class="page-item disabled"><span class="page-
                    link">{% trans "Previous" %}</span></li>
                {% endif %}

                {% for page_number in object_list.paginator
                .page_range %}
                    {% if page_number == object_list.number %}
                        <li class="page-item active">
                            <span class="page-link">{{ page_number }}
                                <span class="sr-only">{% trans 
                                "(current)" %}</span>
                            </span>
                        </li>
                    {% else %}
                        <li class="page-item">
                            <a class="page-link" href="{% modify_query 
                            page=page_number %}">
                                {{ page_number }}</a>
                        </li>
                    {% endif %}
                {% endfor %}

                {% if object_list.has_next %}
                    <li class="page-item"><a class="page-link" href="{% 
                modify_query page=object_list.next_page_number %}">
                        {% trans "Next" %}</a></li>
                {% else %}
                    <li class="page-item disabled"><span class="page-
                    link">{% trans "Next" %}</span></li>
                {% endif %}
            </ul>
        </nav>
    {% endif %}
    ```
## Composing class-based views
- class-based views are useful when you want to create reusable modular views or combine views of the generic mixins
- eg. class based view inheriting the Django View class and overriding it's get() method:
    ```
        # myproject/apps/ideas/views.py
        from django.shortcuts import render, redirect, get_object_or_404
        from django.conf import settings
        from django.core.paginator import (EmptyPage, PageNotAnInteger, Paginator)
        from django.views.generic import View

        from .forms import IdeaFilterForm
        from .models import Idea, RATING_CHOICES


        PAGE_SIZE = getattr(settings, "PAGE_SIZE", 24)


        class IdeaListView(View):
            form_class = IdeaFilterForm
            template_name = "ideas/idea_list.html"

            def get(self, request, *args, **kwargs):
                form = self.form_class(data=request.GET)
                qs, facets = self.get_queryset_and_facets(form)
                page = self.get_page(request, qs)
                context = {"form": form, "facets": facets, 
                "object_list": page}
                return render(request, self.template_name, context)

            def get_queryset_and_facets(self, form):
                qs = Idea.objects.order_by("title")
                facets = {
                    "selected": {},
                    "categories": {
                        "authors": form.fields["author"].queryset,
                        "categories": form.fields["category"].queryset,
                        "ratings": RATING_CHOICES,
                    },
                }
                if form.is_valid():
                    filters = (
                        # query parameter, filter parameter
                        ("author", "author"),
                        ("category", "categories"),
                        ("rating", "rating"),
                    )
                    qs = self.filter_facets(facets, qs, form, filters)
                return qs, facets

            @staticmethod
            def filter_facets(facets, qs, form, filters):
                for query_param, filter_param in filters:
                    value = form.cleaned_data[query_param]
                    if value:
                        selected_value = value
                        if query_param == "rating":
                            rating = int(value)
                            selected_value = (rating,  
                            dict(RATING_CHOICES)[rating])
                        facets["selected"][query_param] = selected_value
                        filter_args = {filter_param: value}
                        qs = qs.filter(**filter_args).distinct()
                return qs

            def get_page(self, request, qs):
                paginator = Paginator(qs, PAGE_SIZE)
                page_number = request.GET.get("page")
                try:
                    page = paginator.page(page_number)
                except PageNotAnInteger:
                    page = paginator.page(1)
                except EmptyPage:
                    page = paginator.page(paginator.num_pages)
                return page
    ```
- url registered as so:
    ```
        urlpatterns = [
            path("", IdeaListView.as_view(), name="idea_list"),
            # other paths…
        ]
    ```
## Generating PDF documents
- dependencies:
    - cairo pango gdk-pixbuf libffi
    - pip install WeasyPrint==48
    - pip install django-qr-code==1.0.0
- Add "qr_code" to INSTALLED_APPS in the settings
- view to generate pdf
    ```
        # myproject/apps/ideas/views.py
        from django.shortcuts import get_object_or_404
        from .models import Idea

        def idea_handout_pdf(request, pk):
            from django.template.loader import render_to_string
            from django.utils.timezone import now as timezone_now
            from django.utils.text import slugify
            from django.http import HttpResponse

            from weasyprint import HTML
            from weasyprint.fonts import FontConfiguration

            idea = get_object_or_404(Idea, pk=pk)
            context = {"idea": idea}
            html = render_to_string(
                "ideas/idea_handout_pdf.html", context
            )

            response = HttpResponse(content_type="application/pdf")
            response[
                "Content-Disposition"
            ] = "inline; filename={date}-{name}-handout.pdf".format(
                date=timezone_now().strftime("%Y-%m-%d"),
                name=slugify(idea.translated_title),
            )

            font_config = FontConfiguration()
            HTML(string=html).write_pdf(
                response, font_config=font_config
            )

            return response
    ```
- add view to urls config
    ```
        urlpatterns = [
        # URL configurations…
        path(
            "<uuid:pk>/handout/",
            idea_handout_pdf,
            name="idea_handout",
        ),
     ]
    ```
- template for pdf generation
    ```
        {# ideas/idea_handout_pdf.html #}
        {% extends "base_pdf.html" %}
        {% load i18n qr_code %}

        {% block content %}
            <h1 class="h3">{% trans "Handout" %}</h1>
            <h2 class="h1">{{ idea.translated_title }}</h2>
            <img src="{{ idea.picture_large.url }}" alt="" 
            class="img-responsive w-100" />
            <div class="my-3">{{ idea.translated_content|linebreaks|
            urlize }}</div>
            <p>
                {% for category in idea.categories.all %}
                    <span class="badge badge-pill badge-info">
                    {{ category.translated_title }}</span>
                {% endfor %}
            </p>
            <h4>{% trans "See more information online:" %}</h4>
            {% qr_from_text idea.get_url size=20 border=0 as svg_code %}
            <img alt="" src="data:image/svg+xml,
            {{ svg_code|urlencode }}" />
            <p class="mt-3 text-break">{{ idea.get_url }}</p>
        {% endblock %}
    ```
- additionaly, create base pdf template 
    ```
        {# base_pdf.html #}
        <!doctype html>
        {% load i18n static %}
        <html lang="en">
        <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, 
            initial-scale=1, shrink-to-fit=no">

            <!-- Bootstrap CSS -->
            <link rel="stylesheet"      
            href="https://stackpath.bootstrapcdn.com
            /bootstrap/4.3.1/css/bootstrap.min.css"
                integrity="sha384-
                ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY
                /iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

            <title>{% trans "Hello, World!" %}</title>

            <style>
            @page {
                size: "A4";
                margin: 2.5cm 1.5cm 3.5cm 1.5cm;
            }
            footer {
                position: fixed;
                bottom: -2.5cm;
                width: 100%;
                text-align: center;
                font-size: 10pt;
            }
            footer img {
                height: 1.5cm;
            }
            </style>

            {% block meta_tags %}{% endblock %}
        </head>
        <body>
            <main class="container">
                {% block content %}
                {% endblock %}
            </main>
            <footer>
                <img alt="" src="data:image/svg+xml,
                {# url-encoded SVG logo goes here #}" />
                <br />
                {% trans "Printed from MyProject" %}
            </footer>
        </body>
        </html>
    ```
## Implementing a multilingual search with Haystack and Whoosh
- Haystack is a modular search API that supports the Solr, Elasticsearch, Whoosh, and Xapian search engines
- For each model in your project that has to be findable in the search, you need to define an index that will read out the textual information from the models and place it into the backend. 
- setup
    - pip install `django-haystack` and `Whoosh`
    - create an app to contain the search engine and indexes
    ```
    # myproject/apps/search/multilingual_whoosh_backend.py
    from django.conf import settings
    from django.utils import translation
    from haystack.backends.whoosh_backend import (
        WhooshSearchBackend,
        WhooshSearchQuery,
        WhooshEngine,
    )
    from haystack import connections
    from haystack.constants import DEFAULT_ALIAS


    class MultilingualWhooshSearchBackend(WhooshSearchBackend):
        def update(self, index, iterable, commit=True, 
        language_specific=False):
            if not language_specific and self.connection_alias == 
            "default":
                current_language = (translation.get_language() or 
                settings.LANGUAGE_CODE)[
                    :2
                ]
                for lang_code, lang_name in settings.LANGUAGES:
                    lang_code_underscored = lang_code.replace("-", "_")
                    using = f"default_{lang_code_underscored}"
                    translation.activate(lang_code)
                    backend = connections[using].get_backend()
                    backend.update(index, iterable, commit, 
                    language_specific=True)
                translation.activate(current_language)
            elif language_specific:
                super().update(index, iterable, commit)


    class MultilingualWhooshSearchQuery(WhooshSearchQuery):
        def __init__(self, using=DEFAULT_ALIAS):
            lang_code_underscored =   
            translation.get_language().replace("-", "_")
            using = f"default_{lang_code_underscored}"
            super().__init__(using=using)


    class MultilingualWhooshEngine(WhooshEngine):
        backend = MultilingualWhooshSearchBackend
        query = MultilingualWhooshSearchQuery
    ```
    - create the search indexes
    ```
    # myproject/apps/search/search_indexes.py
    from haystack import indexes

    from myproject.apps.ideas.models import Idea


    class IdeaIndex(indexes.SearchIndex, indexes.Indexable):
        text = indexes.CharField(document=True)

        def get_model(self):
            return Idea

        def index_queryset(self, using=None):
            """
            Used when the entire index for model is updated.
            """
            return self.get_model().objects.all()

        def prepare_text(self, idea):
            """
            Called for each language / backend
            """
            fields = [
                idea.translated_title, idea.translated_content
            ]
            fields += [
                category.translated_title 
                for category in idea.categories.all()
            ]
            return "\n".join(fields)
    ```
    - Configure the settings to use MultilingualWhooshEngine
        ```
        # myproject/settings/_base.py
        import os
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__)
        )))

        #…

        INSTALLED_APPS = [
            # contributed
            # …
            # third-party
            # …
            "haystack",<--------
            # local
            "myproject.apps.core",
            "myproject.apps.categories",
            "myproject.apps.ideas",
            "myproject.apps.search",<--------
        ]
        ...

        HAYSTACK_CONNECTIONS = {}
        for lang_code, lang_name in LANGUAGES:
        lang_code_underscored = lang_code.replace("-", "_")
        HAYSTACK_CONNECTIONS[f"default_{lang_code_underscored}"] = {
        "ENGINE":   
        "myproject.apps.search.multilingual_whoosh_backend
        .MultilingualWhooshEngine",
        "PATH": os.path.join(BASE_DIR, "tmp", 
        f"whoosh_index_{lang_code_underscored}"),
        }
        lang_code_underscored = LANGUAGE_CODE.replace("-", "_")
        HAYSTACK_CONNECTIONS["default"] = HAYSTACK_CONNECTIONS[
        f"default_{lang_code_underscored}"
        ]
        ```
    - register the url
    - create a template for displaying results
    - Call the rebuild_index management command to index the database data
        ```
        python manage.py rebuild_index --noinput
        ```
## Implementing a multilingual search with Elasticsearch DSL
- install elasticsearch on machine, then `pip install django-elasticsearch-dsl==XXX` with same version installed on machine replacing the `XXX` part
- add `django_elasticsearch_dsl` to INSTALLED_APPS in settings, and add elasticsearch config:
    ```
        ELASTICSEARCH_DSL={
            'default': {
                'hosts': 'localhost:9200'
            },
        }
    ```
- the search index will be defined in one of the apps
    - this will include a number of `prepare_` methods that prepare data for the index
- create a form and view for searching, and a template to display results
- build the index with `python manage.py search_index --rebuild`
# Chpt.4 Templates and JavaScript
## Arranging the base.html template
```
    # myproject/settings/_base.py
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "myproject", "templates")],<-------
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                ]
            },
        }
    ]
```
- Setup
    1. In the root directory of your templates, create a base.html file
        ```
            {# base.html #}
            <!doctype html>
            {% load i18n static %}
            <html lang="en">
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-
                scale=1, shrink-to-fit=no" />
                <title>{% block head_title %}{% endblock %}</title>
                {% include "misc/includes/favicons.html" %}
                {% block meta_tags %}{% endblock %}

                <link rel="stylesheet"
                    href="https://stackpath.bootstrapcdn.com/bootstrap
                    /4.3.1/css/bootstrap.min.css"
                    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784
                    /j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
                    crossorigin="anonymous" />
                <link rel="stylesheet"
                    href="{% static 'site/css/style.css' %}"
                    crossorigin="anonymous" />

                {% block css %}{% endblock %}
                {% block extra_head %}{% endblock %}
            </head>
            <body>
                {% include "misc/includes/header.html" %}
                <div class="container my-5">
                    {% block content %}
                        <div class="row">
                            <div class="col-lg-4">{% block sidebar %}
                            {% endblock %}</div>
                            <div class="col-lg-8">{% block main %}
                            {% endblock %}</div>
                        </div>
                    {% endblock %}
                </div>
                {% include "misc/includes/footer.html" %}
                <script src="https://code.jquery.com/jquery-3.4.1.min.js"
                        crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js
                /1.14.7/umd/popper.min.js"
                        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj
                        9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
                        crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap
                /4.3.1/js/bootstrap.min.js"
                        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6Vrj
                        IEaFf/nJGzIxFDsf4x0xIM+B07jRM"
                        crossorigin="anonymous"></script>
                {% block js %}{% endblock %}
                {% block extra_body %}{% endblock %}
            </body>
            </html>
        ```
    2. Under misc/includes, create a template including all the versions of the favicon
        ```
            {# misc/includes/favicon.html #}
            {% load static %}
            <link rel="icon" type="image/png" href="{% static 'site/img/favicon-32x32.png' %}" sizes="32x32"/>
            <link rel="icon" type="image/png" href="{% static 'site/img/favicon-16x16.png' %}" sizes="16x16"/>
        ```
    3. Create the templates misc/includes/header.html and misc/includes/footer.html with your website's header and footer
- can have separate base templates for other layouts as well, such as single-column, two-column, and three-column layouts, where each extends base.html and overwrites the blocks as needed.
- <body> of base template above has these features:
    - header of the website. That's where you can put your logo, website title, and main navigation.
    - main container containing a content block placeholder, which is to be filled by extending the templates.
    - Inside the container, there is the content block, which contains the sidebar and main blocks. 
        - In child templates, when we need a layout with a sidebar. We will overwrite the sidebar and main blocks, but, when we need the full-width content, we will overwrite the content block.
    - footer of the website. That's where you can have copyright information and links to important meta pages, such as privacy policy, terms of use, contact form, and others.
    - jQuery and Bootstrap scripts. Extensible JavaScript blocks are included here at the end of the <body> following the best practices for page-load performance, much like those for the style sheets included in the <head>.
    - blocks for additional JavaScript and extra HTML, such as HTML templates for JavaScript or hidden modal dialogs.
## Using Django Sekizai
- normally you would use template inheritance to overwrite blocks from parent templates to include styles or scripts to the HTML document. This means that every main template of each view should be aware of all content that is inside; however, sometimes it is much more convenient to let the included templates decide what styles and scripts to load. It is possible to do this with Django Sekizai.
- install `django-classy-tags` and `django-sekizai` 
- add `sekizai` to INSTALLED_APPS in settings
- add `sekizai.context_processors.sekizai` to `context_processors` section in settings TEMPLATE section
- setup:
    - at the beginning of base template, load sekizai_tags library
    ```
     {# base.html #}
    <!doctype html>
    {% load i18n static sekizai_tags %}
    ```
    - in same file, at end of <head> section add `{% render_block "css" %}` template tag
    - at bottom of <body> section add `{% render_block "js" %}` template tag
- now, in any template that you want to add css or styling to, use `addtoblock` tags:
    ```
    {% load static sekizai_tags %}

    <div>Sample widget</div>

    {% addtoblock "css" %}
    <link rel="stylesheet" href="{% static 'site/css/sample-widget.css' 
    %}"/>
    {% endaddtoblock %}

    {% addtoblock "js" %}
    <script src="{% static 'site/js/sample-widget.js' %}"></script>
    {% endaddtoblock %}
    ```
## Exposing settings in JavaScript
- have the `django.template.context_processors.request` in the TEMPLATES['OPTIONS']['context_processors'] setting of settings.py
- setup
    1. In the views.py of your core app, create a js_settings() view that returns a response of the JavaScript content type
        ```
            # myproject/apps/core/views.py
            import json
            from django.http import HttpResponse
            from django.template import Template, Context
            from django.views.decorators.cache import cache_page
            from django.conf import settings

            JS_SETTINGS_TEMPLATE = """
            window.settings = JSON.parse('{{ json_data|escapejs }}');
            """

            @cache_page(60 * 15)
            def js_settings(request):
                data = {
                    "MEDIA_URL": settings.MEDIA_URL,
                    "STATIC_URL": settings.STATIC_URL,
                    "DEBUG": settings.DEBUG,
                    "LANGUAGES": settings.LANGUAGES,
                    "DEFAULT_LANGUAGE_CODE": settings.LANGUAGE_CODE,
                    "CURRENT_LANGUAGE_CODE": request.LANGUAGE_CODE,
                }
                json_data = json.dumps(data)
                template = Template(JS_SETTINGS_TEMPLATE)
                context = Context({"json_data": json_data})
                response = HttpResponse(
                    content=template.render(context),
                    content_type="application/javascript; charset=UTF-8",
                )
                return response
        ```
    2. Add this to urls config
        ```
            urlpatterns = i18n_patterns(
            # other URL configuration rules…
            path("js-settings/", core_views.js_settings, 
            name="js_settings"),
            )
        ```
    3. Load the JavaScript-based view in the frontend by adding it at the end of the base.html template
        ```
            {# base.html #}    

                {# … #}

                <script src="{% url 'js_settings' %}"></script>
                {% block js %}{% endblock %}
                {% render_block "js" %}
                {% block extra_body %}{% endblock %}
            </body>
            </html>
        ```
- in `js_settings()` we build a dictionary of settings that we want to pass to the browser, convert the dictionary to JSON, and render a template for a JavaScript file that parses the JSON and assigns the result to the window.settings variable
# Chpt.5 Custom Template Filters and Tags
- Django allows you to add your own template filters and tags to your apps. 
    - Custom filters or tags should be located in a `template-tag` library file under the templatetags Python package in your app. Your template-tag library can then be loaded in any template with the `{% load %}` template tag
## Following conventions for your own template filters and tags
1. Don't create or use custom template filters or tags when the logic for the page fits better in the view, context processors, or model methods. When your content is context-specific, such as a list of objects or an object-detail view, load the object in the view. If you need to show some content on nearly every page, create a context processor. Use custom methods of the model instead of template filters when you need to get some properties of an object that are not related to the context of the template.

2. Name the template-tag library with the _tags suffix. When your template-tag library is named differently than your app, you can avoid ambiguous package-importing problems.
# Chpt.7 Security and Performance
## Authenticating with Auth0
- create an Auth0 application at https://auth0.com/​ and configure it by following the instructions there.
- install `python-social-auth`, `python-jose`, `python-dotenv`
- add `"social_django",` to settings `INSTALLED_APPS`
- add follwing OAuht settings to settings file
    ```
    SOCIAL_AUTH_AUTH0_DOMAIN = get_secret("AUTH0_DOMAIN")
    SOCIAL_AUTH_AUTH0_KEY = get_secret("AUTH0_KEY")
    SOCIAL_AUTH_AUTH0_SECRET = get_secret("AUTH0_SECRET")
    SOCIAL_AUTH_AUTH0_SCOPE = ["openid", "profile", "email"]
    SOCIAL_AUTH_TRAILING_SLASH = False
    ```
- create backend for OAuth connection
    ```
    
    # myproject/apps/external_auth/backends.py
    from urllib import request
    from jose import jwt
    from social_core.backends.oauth import BaseOAuth2

    class Auth0(BaseOAuth2):
        """Auth0 OAuth authentication backend"""

        name = "auth0"
        SCOPE_SEPARATOR = " "
        ACCESS_TOKEN_METHOD = "POST"
        REDIRECT_STATE = False
        EXTRA_DATA = [("picture", "picture"), ("email", "email")]

        def authorization_url(self):
            return "https://" + self.setting("DOMAIN") + "/authorize"

        def access_token_url(self):
            return "https://" + self.setting("DOMAIN") + "/oauth/token"

        def get_user_id(self, details, response):
            """Return current user id."""
            return details["user_id"]

        def get_user_details(self, response):
            # Obtain JWT and the keys to validate the signature
            id_token = response.get("id_token")
            jwks = request.urlopen(
                "https://" + self.setting("DOMAIN") + "/.well-
                known/jwks.json"
            )
            issuer = "https://" + self.setting("DOMAIN") + "/"
            audience = self.setting("KEY")  # CLIENT_ID
            payload = jwt.decode(
                id_token,
                jwks.read(),
                algorithms=["RS256"],
                audience=audience,
                issuer=issuer,
            )
            first_name, last_name = (payload.get("name") or 
            " ").split(" ", 1)
            return {
                "username": payload.get("nickname") or "",
                "first_name": first_name,
                "last_name": last_name,
                "picture": payload.get("picture") or "",
                "user_id": payload.get("sub") or "",
                "email": payload.get("email") or "",
            }
    ```
- add backend to `AUTHENTICATION_BACKENDS` setting
    ```
    # myproject/settings/_base.py
    AUTHENTICATION_BACKENDS = {
        "myproject.apps.external_auth.backends.Auth0",
        "django.contrib.auth.backends.ModelBackend",
    }
    ```
- create context processesor so available from any template
    ```
    # myproject/apps/external_auth/context_processors.py
    def auth0(request):
        data = {}
        if request.user.is_authenticated:
            auth0_user = request.user.social_auth.filter(
                provider="auth0",
            ).first()
            data = {
                "auth0_user": auth0_user,
            }
        return data
    ```
- register processor in settings
    ```
    # myproject/settings/_base.py
    TEMPLATES = [
        {
            "BACKEND": 
            "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "myproject", "templates")],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors
                    .messages",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "myproject.apps.core.context_processors
                    .website_url",
                    "myproject.apps.external_auth
                .context_processors.auth0",
                ]
            },
        }
    ]
    ```
- create index page, dashboard, logout views
    ```
    # myproject/apps/external_auth/views.py
    from urllib.parse import urlencode

    from django.shortcuts import render, redirect
    from django.contrib.auth.decorators import login_required
    from django.contrib.auth import logout as log_out
    from django.conf import settings


    def index(request):
        user = request.user
        if user.is_authenticated:
            return redirect(dashboard)
        else:
            return render(request, "index.html")


    @login_required
    def dashboard(request):
        return render(request, "dashboard.html")


    def logout(request):
        log_out(request)
        return_to = urlencode({"returnTo": 
        request.build_absolute_uri("/")})
        logout_url = "https://%s/v2/logout?client_id=%s&%s" % (
            settings.SOCIAL_AUTH_AUTH0_DOMAIN,
            settings.SOCIAL_AUTH_AUTH0_KEY,
            return_to,
        )
        return redirect(logout_url)
    ```
- create index template
    ```
    {# index.html #}
    {% extends "base.html" %}
    {% load i18n utility_tags %}

    {% block content %}
    <div class="login-box auth0-box before">
        <h3>{% trans "Please log in for the best user experience" %}</h3>
        <a class="btn btn-primary btn-lg" href="{% url "social:begin" 
        backend="auth0" %}">{% trans "Log in" %}</a>
    </div>
    {% endblock %}
    ```
- dashboard
    ```
    {# dashboard.html #}
    {% extends "base.html" %}
    {% load i18n %}

    {% block content %}
        <div class="logged-in-box auth0-box logged-in">
            <img alt="{% trans 'Avatar' %}" src="{{ 
            auth0_user.extra_data.picture }}" 
            width="50" height="50" />
            <h2>{% blocktrans with name=request.user
            .first_name %}Welcome, {{ name }}
            {% endblocktrans %}!</h2>

            <a class="btn btn-primary btn-logout" href="{% url 
            "auth0_logout" %}">{% trans "Log out" %}</a>
        </div>
    {% endblock %}
    ```
- update URL rules
    ```
    # myproject/urls.py
    from django.conf.urls.i18n import i18n_patterns
    from django.urls import path, include

    from myproject.apps.external_auth import views as external_auth_views

    urlpatterns = i18n_patterns(
        path("", external_auth_views.index, name="index"),
        path("dashboard/", external_auth_views.dashboard, 
        name="dashboard"),
        path("logout/", external_auth_views.logout, 
        name="auth0_logout"),
        path("", include("social_django.urls")),
        # …
    )
    ```
- add login url settings
    ```
    LOGIN_URL = "/login/auth0"
    LOGIN_REDIRECT_URL = "dashboard"
    ```

## Caching the method return value
- If you call a model method with heavy calculations or database queries multiple times in the request-response cycle, the performance of the view might become very slow
    - you can use a pattern to cache the return value of a method for later repetitive use.
- basic pattern:
    ```
    class SomeModel(models.Model):
        def some_expensive_function(self):
            if not hasattr(self, "_expensive_value_cached"):
                # do some heavy calculations...
                # ... and save the result to result variable
                self._expensive_value_cached = result
            return self._expensive_value_cached
    ```
    -  can now use something such as {{ object.some_expensive_function }} in the header and footer of a template, and the time-consuming calculations will be done just once.
- example:
    ```
    class ViralVideo(CreationModificationDateBase, UrlBase):
        embed_code = models.TextField(
            _("YouTube embed code"),
            blank=True)

        # …

        def get_thumbnail_url(self):
            if not hasattr(self, "_thumbnail_url_cached"):
                self._thumbnail_url_cached = ""
                url_pattern = re.compile(
                    r'src="https://www.youtube.com/embed/([^"]+)"'
                )
                match = url_pattern.search(self.embed_code)
                if match:
                    video_id = match.groups()[0]
                    self._thumbnail_url_cached = (
                        f"https://img.youtube.com/vi/{video_id}/0.jpg"
                    )
            return self._thumbnail_url_cached
    ```
- approach only works if the method is called without arguments so that the result will always be the same. But if input varies, there is a decorator ( `@lru_cache ` ) we can use to provide basic Least Recently Used (LRU) caching of method calls based on a hash of the arguments (at least those that are hashable).
    - ```from functools import lru_cache```
    - used in above example:
        ```
        # myproject/apps/viral_videos/models.py
        from functools import lru_cache
        # …

        class ViralVideo(CreationModificationDateMixin, UrlMixin):
            # …
            @lru_cache
            def get_thumbnail_url(self):
                # …
        ```
## Using Redis to cache Django views
- ```brew install redis```
- install in virtualenv
    ```
    pip install redis==3.3.11
    pip install hiredis==1.0.1
    pip install django-redis-cache==2.1.0
    ```
- set CACHES in settings
    ```
    # myproject/settings/_base.py
    CACHES = {
        "redis": {
            "BACKEND": "redis_cache.RedisCache",
            "LOCATION": [get_secret("CACHE_LOCATION")],
            "TIMEOUT": 60, # 1 minute
            "KEY_PREFIX": "myproject",
        },
    }
    CACHES["default"] = CACHES["redis"]
    ```
- Make sure that you have CACHE_LOCATION set to "localhost:6379" in your secrets or environment variables.
- use in view like so:
    ```
    # myproject/apps/viral_videos/views.py
    from django.shortcuts import render
    from django.views.decorators.cache import cache_page
    from django.views.decorators.vary import vary_on_cookie

    @vary_on_cookie
    @cache_page(60)
    def viral_video_detail(request, pk):
        # …
        return render(
            request,
            "viral_videos/viral_video_detail.html",
            {'video': video}
        )
    ```
- Redis is a key-value store, and when used for caching, it generates the key for each cached page based on the full URL. 
    - When two visitors access the same page simultaneously, the first visitor's request would receive the page generated by the Python code, and the second one would get the same HTML code but from the Redis server
- `@vary_on_cookie` decorator ensures each user treated separately

## Creating hierarchical categories with django-mptt
- Modified Preorder Tree Traversal (MPTT)
- used for build forums, threaded comments, and categorization systems, there will be a moment when you need to save hierarchical structures in a database. 
- MPTT allows you to read tree structures without recursive calls to the database.
- setup
    - `pip install django-mptt==0.10.0`
    - add `mptt` to `INSTALLED_APPS` list in settings
- in this example, create a hierarchical Category model and tie it to the Idea model, which will have a many-to-many relationship with the categories
    - Category model will extend `mptt.models.MPTTModel` and `CreationModificationDateBase` (mixin defined in Chapter 2).
        - model will need to have a parent field of the TreeForeignKey type and a title field.
        ```
            # myproject/apps/ideas/models.py
            from django.db import models
            from django.utils.translation import ugettext_lazy as _
            from mptt.models import MPTTModel
            from mptt.fields import TreeForeignKey

            from myproject.apps.core.models import CreationModificationDateBase


            class Category(MPTTModel, CreationModificationDateBase):
                parent = TreeForeignKey(
                    "self", on_delete=models.CASCADE, 
                    blank=True, null=True, related_name="children"
                )
                title = models.CharField(_("Title"), max_length=200)

                class Meta:
                    ordering = ["tree_id", "lft"]
                    verbose_name = _("Category")
                    verbose_name_plural = _("Categories")

                class MPTTMeta:
                    order_insertion_by = ["title"]

                def __str__(self):
                    return self.title
        ```
    - Ideas model will include categories field of `TreeManyToManyField` type
        ```
        # myproject/apps/ideas/models.py
        from django.utils.translation import gettext_lazy as _

        from mptt.fields import TreeManyToManyField

        from myproject.apps.core.models import CreationModificationDateBase, UrlBase


        class Idea(CreationModificationDateBase, UrlBase):
            # …
            categories = TreeManyToManyField(
                "categories.Category",
                verbose_name=_("Categories"),
                related_name="category_ideas",
            )
        ```
    - run `makemigrations` and `migrate` 

- MPTTModel mixin will add the tree_id, lft, rght, and level fields to the Category model
    - The lft and rght fields store the left and right values used in the MPTT algorithms.
        - determining children of node in tree `descendants = (right - left - 1) / 2`
    - The level field stores the node's depth in the tree. The root node will be level 0.

- retrieval commands
    - get ancestors of a node
        ```
        ancestor_categories = category.get_ancestors(
            ascending=False,
            include_self=False,
        )
        ```

    - children = category.get_children()

    - descendants = category.get_descendants(include_self=False)

    - descendants_count = category.get_descendant_count()

    - siblings = category.get_siblings(include_self=False)

    - previous_sibling = category.get_previous_sibling()
    - next_sibling = category.get_next_sibling()

- other methods
    - category.is_root_node()
    - category.is_child_node()
    - category.is_leaf_node()
    - insert_at()  
    - move_to()
## Rendering categories in a template with django-mptt
- use the `{% recursetree %}` template tag from the django-mptt app
- Pass `QuerySet` of your hierarchical categories to the template and then use the `{% recursetree %}` template tag
    - create a view that loads everything and passes to a template
        ```
        # myproject/apps/categories/views.py
        from django.views.generic import ListView

        from .models import Category

        class IdeaCategoryList(ListView):
            model = Category
            template_name = "categories/category_list.html"
            context_object_name = "categories"
        ```
    - template to output hierarchies
        ```
        {# categories/category_list.html #}
        {% extends "base.html" %}
        {% load mptt_tags %}

        {% block content %}
            <ul class="root">
                {% recursetree categories %}
                    <li>
                        {{ node.title }}
                        {% if not node.is_leaf_node %}
                            <ul class="children">
                                {{ children }}
                            </ul>
                        {% endif %}
                    </li>
                {% endrecursetree %}
            </ul>
        {% endblock %}
        ```
    - create the URL rules
        ```
        # myproject/urls.py
        from django.conf.urls.i18n import i18n_patterns
        from django.urls import path

        from myproject.apps.categories import views as categories_views

        urlpatterns = i18n_patterns(
            # …
            path(
                "idea-categories/",
                categories_views.IdeaCategoryList.as_view(),
                name="idea_categories",
            ),
        )
        ```
- If hierarchical structure is very complex, with more than 20 levels, it is recommended to use the `{% full_tree_for_model %}` and `{% drilldown_tree_for_node %}` iterative tags
## Using a single selection field to choose a category in forms with django-mptt
- if you want to show category selection in a form, django-mptt has a special `TreeNodeChoiceField` form field that you can use to show the hierarchical structures in a selected field.
- in a form, create a categories field like so:
    ```
    category = TreeNodeChoiceField(
        label=_("Category"),
        required=False,
        queryset=Category.objects.all(),
        level_indicator=mark_safe("&nbsp;&nbsp;&nbsp;&nbsp;")
    )
    ...
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        author_field = layout.Field("author")
        category_field = layout.Field("category")<----
        rating_field = layout.Field("rating")
        submit_button = layout.Submit("filter", _("Filter"))
        actions = bootstrap.FormActions(submit_button)

        main_fieldset = layout.Fieldset(
            _("Filter"),
            author_field,
            category_field,<----
            rating_field,
            actions,
        )

        self.helper = helper.FormHelper()
        self.helper.form_method = "GET"
        self.helper.layout = layout.Layout(main_fieldset)
    ```
- render in template using crispy-tags ( from django-crispy-forms mod )
    ```
    {# ideas/idea_list.html #}
    {% extends "base.html" %}
    {% load i18n utility_tags crispy_forms_tags %}

    {% block sidebar %}
        {% crispy form %}
    {% endblock %}

    {% block main %}
        {# … #}
    {% endblock %}
    ```
- now rendered category dropdown will be like:
    ```
    category 1
        1
        2
        3
    category 2
        4
        5
        6
    ```  
# Chpt.8 Importing and Exporting data
## Importing data from a local CSV file
- eg scenario: have `Music` app with a Song model containing uuid, artist, title, url, and image fields
    - admin function for Songs
        ```
        # myproject/apps/music/admin.py
        from django.contrib import admin
        from .models import Song

        @admin.register(Song)
        class SongAdmin(admin.ModelAdmin):
            list_display = ["title", "artist", "url"]
            list_filter = ["artist"]
            search_fields = ["title", "artist"]
        ```
    - form for validating and creating songs
        ```
        # myproject/apps/music/forms.py
        from django import forms
        from django.utils.translation import ugettext_lazy as _
        from .models import Song

        class SongForm(forms.ModelForm):
            class Meta:
                model = Song
                fields = "__all__" 
        ```
    - In the music app, create a `management` directory and then a `commands` directory in the new `management` directory. Put empty __init__.py files in both new directories to make them Python packages.
    - Add `import_music_from_csv.py` to `commands`
    ```
    # myproject/apps/music/management/commands/import_music_from_csv.py
    from django.core.management.base import BaseCommand

    class Command(BaseCommand):
        help = (
            "Imports music from a local CSV file. "
            "Expects columns: artist, title, url"
        )
        SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

        def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument("file_path", nargs=1, type=str)

        def handle(self, *args, **options):
            self.verbosity = options.get("verbosity", self.NORMAL)
            self.file_path = options["file_path"][0]
            self.prepare()
            self.main()
            self.finalize()
    
        def prepare(self):
            self.imported_counter = 0
            self.skipped_counter = 0
        
        def main(self):
            import csv
            from ...forms import SongForm

            if self.verbosity >= self.NORMAL:
                self.stdout.write("=== Importing music ===")

            with open(self.file_path, mode="r") as f:
                reader = csv.DictReader(f)
                for index, row_dict in enumerate(reader):
                    form = SongForm(data=row_dict)
                    if form.is_valid():
                        song = form.save()
                        if self.verbosity >= self.NORMAL:
                            self.stdout.write(f" - {song}\n")
                        self.imported_counter += 1
                    else:
                        if self.verbosity >= self.NORMAL:
                            self.stderr.write(
                                f"Errors importing song "
                                f"{row_dict['artist']} - 
                                {row_dict['title']}:\n"
                            )
                            self.stderr.write(f"{form.errors.as_json()}\n")
                        self.skipped_counter += 1
        
        def finalize(self)
            if self.verbosity >= self.NORMAL:
                self.stdout.write(f"-------------------------\n")
                self.stdout.write(f"Songs imported:         
                {self.imported_counter}\n")
                self.stdout.write(f"Songs skipped: 
                {self.skipped_counter}\n\n")
    ```
    - run command: `python manage.py import_music_from_csv data/music.csv`