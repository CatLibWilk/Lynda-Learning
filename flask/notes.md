## chp1
Flask (microservice for website and api dev) uses:  
- jinja2 template engine
- werkzeug WSGI (webserver gateway interface) toolkit 

## routing (see Video 1.3 app.py file for full CRUD examples)
- can be done in multiple ways  
    - with @app.route decorator:  
        - eg. @app.route("/api", methods=["GET"])...
    - with `add_url_rule` method:  
        - 1st parameter (/api/candidate) - route path  
        -  2nd parameter (candidate) - endpoint  
	    - 3rd parameter (candidate) - function which is executed  
        - app.add_url_rule('/api/candidate', 'candidate', candidate)  

## using templates (see section 1, video 1.4 for templates and static code)
- templating uses Jinja, which uses block expressions (like handlebar/express)
    - eg. { %block head % }...{ %endblock% }
    - double {{}} used for string-literal-like things
        - eg. `<li><a href="{{url_for('page_index')}}">Home</a></li>`
    - use `extends` keyword to build out from a base template for another page
        - eg. `candidate.html` extends `layout.html`
        - defines the base template and then can override previously-defined blocks
    - `render template` method used to render pages
    - `add_url_rule` used to set up routes
    - to use a method as a template filter (eg. the senior_candidate function in the app.py file), must append @app.template_filter(name_of_filter) decorator 


### From Full-stack Web Dev Flask course
- structure of application in this course is:
    - top: overall directory holding everyting, containing:
        - `requirements.txt`
        - virtual environment 
        - `.flaskenv` file with environment variables
        - `application` package with the app scripts, static files and template (see below)
        - 
- application package (directory with application files) includes:
    - `__init__.py` file
    - templates directory
    - static directory (used for images/js/css etc.)

- `includes`
    - create `includes` directory in the static folder, can use include to use same element across all pages, eg. a footer
        - use code block to include: `{ %include "includes/footer.html" % }