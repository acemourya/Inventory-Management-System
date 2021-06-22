# Hosting django project:

## 1. Set up the virtual environment -

Make sure that virtualenv package is already installed. If not, install it using the following command:
```bash
$ pip3 install virtualenv
```
Now, create the virtual environment:
```bash
$ virtualenv venv -p python3
```
Activate the virtual environment:
```bash
$ source ./venv/bin/activate
```
## 2. First check and set all dependency of your project present or not in venv. like: packages. 


## 3. Run these commands in vir-env.

    $ pip3 install gunicorn whitenoise

## 4. Create files with name:
    
    1. "Procfile" inside code: (directory_name:- The project main server exist)
        web: gunicorn directory_name.wsgi --log-file -

    2. "runtime.txt" inside write (python version)
        python-3.8.5

    3. "Readme.md" and ".gitignore" file also.

    4. "static" folder where all js, css and imager store in django project main dir.
    and load in "html" files where you want to use it by :
    
        {% load static %}
        <head>
            <link rel="stylesheet" type="text/css" href="{% static 'css/main.css' %}">
        </head>

    Note: if it is not req. any css or other thing, leave it empty static folder. but static folder necessary to host.

    5. Optional: In project create custom error handler by creating these files.

    templates/ 400.html
                403.html
                404.html
                500.html

    inside: 
        <!-- Extend base.html file -->
        {% extends 'base.html' %}

        {% block content %}
            <div class="jumbotron">
            <h1 class="display-4">Page Not Found</h1>
            <p class="lead">Sorry, This page is missing or does not exist</p>
            <hr class="my-4">
            <p class="lead">
                <a class="btn btn-primary btn-lg" href="../" role="button">Go to home page</a>
            </p>
            </div>
        {% endblock content%}            





## 5. Run these commands in vir-env.

    $ pip3 freeze > requirements.txt

## 6. login heroku make app on browser with python mode
   

## 7. Settings.py

    import os

    DEBUG = False

    ALLOWED_HOSTS = ['host-domain_name','localhost', '127.0.0.1']

    MIDDLEWARE = [
        'whitenoise.middleware.WhiteNoiseMiddleware',]

    TEMPLATES = [
        {
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
        }
        ]    

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]  

    Domain_name: "demo.herokuapp.com"
    
## 8. Login in your terminal and upload on heroku.

    $ git init
    $ heroku login
    $ heroku git: remote -a heroku_app_name
    $ git add .
    $ git commit -am "make it better"
    $ git checkout -b main
    $ git branch -D master
    $ git push heroku main
    
# Importants points: 1, 2, 3, 4.1, 4.2, 4.3, 5, 6, 7, 8    
