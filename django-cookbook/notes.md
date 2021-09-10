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