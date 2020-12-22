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

- if/else codeblocks
    - wrap html elements in `{% if [something] %}...{% else %}...{% end %}`

- `render_template` params
    - after the name of the template to render, can pass other arguments, such as a variable to be used in an if/else block 

- `url_for`
    - used for dynamic links, ie. in a navbar, the <li>'s `href` could point to a static file to render, like `index.html` or `contact.html`.  Then if the filename changes you need to manually update the links. 
        - instead use `href="{{ use_url(func_name) }}"`
        - eg.
            - if the function that returns `render_tempate('index.html')` = `def index():`
                - then a list item that links to that page will look like:  
                    - `<li href="{{ use_url(index) }}">Homepage</li>

## Templating
- base template
    - create html file with the things that will be the same across all pages (eg. the <head> outer <html> etc.)
    - include `{% block content %}...{% endblock %}` wrapper for where unique content from other pages will go
    - then on unique pages ( ie. `child templates` ), put `{% extends "name_of_base_template" %}` at top of html file
        - wrap unique content with `{% block content %}...{% endblock %}` (n.b. "content" in block content can be whatever keyword you use in the base template file, but `content` is standard)

- passing data to template
    - can pass args/data to template from render function by adding to `render_template` function
        - eg. `return render_template( 'index.html', homepage_data )`
    - in template, iterate over passed-in data with forloop block `{% for data in homepage_data %}...{% endfor %}`
        - within forloop, use double-bracket expression to dynamically insert data into html elements
            - eg. `<td scope="row">{{ homepage_data["course_name"] }}</td>`
    - for things like adding "active" class to a button in a navbar for page you're currently on, can add if block to an html element
        - eg.  
        ```
        render_template('index.html', index=True)`... 
        <li class="nav-item"><a href="{{ url_for('index')" class="nav-link {% if index %}active{% endif %}"}}>Home</a></li>
        ```

## URL variables
- can pass variables through URL ( eg. course id at end of `example.com/courses/111` ) like so:  
    - @app.routes('/courses/<id>') and then the variable declared as arg of function that renders template
        - def `courses(id):`
    - then pass within the `render_template` function call  
        - eg. `return render_template('courses.html', id=id)  
    - and use dynamic declaration (double curly bracket) in template to render  
        - eg. `<h1>Course No. {{ id }}</h1>`

## GET request 
- if you have something like an `enrollment` template, and a route defined for it, you can set up a <form> with attributes `action={{url_for('enrollment')}}` and `method=GET` and then <input> elements with attribute `value={{data['some_data']}}`
    - then in route definitions, in function that renders `enrollment` template, receive data with `request` python objects eg
    ```
    def enrollment():
        id = request.args.get('courseID') ##courseID is value of `name` attribute in form's input element
        name = request.args.get('courseName')

        return render_template("enrollment.html", data={"id":id, "name":name})
    ```
    - and then in template, use dynamic declaration to use data values eg.
        - <p>You are enrolled in {{ data.courseName }} </p>

    - GET will work without explicit declaration of GET method usage in the rendering function (ie enrollment()) decorator, but for others, and if using multiple, need to declare 
    ```
    @app.route('/enrollment', METHODS=['GET', 'POST'])
    def enrollment():...
    ```

## POST
- pretty much the same as GET, but need to explicitly declare the method in the app.route decorator, and to get passed data need to use `request.form.get` instead of `request.args.get`

## connecting MongoDB
- in `__init__.py`:
```
from flask_mongoengine import MongoEngine` in `__init__.py
db = MongoEngine()
db.init_app(app)
```
- in `routes.py`
```
from application import app, db
```
- then to define tables or "documents" in mongod parlance, create classes with `db.Document` passed as arg
```
class User( db.Document ):
    user_id = db.IntField(unique=True)
    name = db.StringField(max_length=50)
```
