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