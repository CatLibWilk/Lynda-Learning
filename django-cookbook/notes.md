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

