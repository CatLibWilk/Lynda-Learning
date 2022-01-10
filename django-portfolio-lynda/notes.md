# Chpt. 2 Creating projects/apps
- in Django, the website you create is the `project`, and it's individual pieces (blog, events page, accounts) are the `apps`
    - create project: `django-admin startproject [name]`
        - will create a [name] directory with the `manage.py` script, and a subdirectory with same name containing the `settings.py`, `urls.py` and wsgi files
    - create app:  `django-admin startapp [name]`
        - must register app in `settings.py` INSTALLED_APPS
## URLS
- can either do all url routing in the main `urls.py` file, or have individual URL settings per app using `include`
    - include setup
        - in main `urls.py` import `include` from `django.urls`
        - in `url_patterns` define route like so
            ```
            ...
                path( '[appname]/', include( '[appname].urls' ) ),
            ...
            ```
            - where path to app in `include` begins at project folder level
        - then, in app folder
            - create `urls.py`, copy imports from main one
            - define paths to be appended to url routing defined in main `urls.py`
                - ex. 
                    - in main `urls.py`: `path( 'jobs/', include( 'jobs.urls' ) ),`
                    - in app `url.py`: `path( '', views.job_home, name=job_home),`
                    - url to reach `job_home` view is `http://domain.com/jobs`

# Chpt. 3 Models/DB
- image storage in django requires installation of `pillow` 

## Postgres setup
- create database for app in postgres

( to `connecting project to postgres` )