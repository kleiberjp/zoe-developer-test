Project Test Zoe Python - Django
==============================

The project inital is based for deployment at openshift server, 
the settings files contains all information need for app django run without troubles, 
if want to run app in server personal create local_settings.py for change enviroment
variables settings and local_database.py for configure connection to db

for run at openshit set at path .openshit/action_hooks/deploy at the command to execute before commit
repository to openshift server, initiali it runs collected_static and set at static all files need for your
files css and js

before run migrate for collect the database an set all necesary tables for django app

there is a version online for web test, just only is access at the url:

http://zoetest-kperez.rhcloud.com/

and for load data in test there is a upload file csv for load csv file with contacts
    

Running on Local Server
----------------------------

Create an `local_settings.py` and change settings variable as this

    import os

    # Local
    DJ_PROJECT_DIR = os.path.dirname(__file__)
    BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)
    
    
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    
    PREPEND_WWW = False
    
    SESSION_COOKIE_DOMAIN = None
    
    ALLOWED_HOSTS = '*'
    
    WEBPAGE = '<NAMES SERVER DEFAULT http://localhost:8000>'
    STATIC_ROOT = ''
    STATIC_URL = '<PATH TO YOUR STATIC FILES>'
    
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, '<PATH TO YOUR STATIC FILES>').replace('\\', '/'),
    )
    
    # Logging
    
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'simple': {
                'format': '%(levelname)s %(message)s',
            },
        },
        'handlers': {
            'console':{
                'level':'DEBUG',
                'class':'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        }
    }


Create an `local_database.py` and change database variable as this:
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.<METHOD OF DATABASE mysql, postgresql_psycopg2, sqlite3>',
            'NAME': '<NAME DATABASE>',
            'USER': '<USER DATABASE>',
            'PASSWORD': '<PASSWORD DATABASE>',
            'HOST': '<HOST DATABASE>',
            'PORT': '<PORT DATABASE>',
        },
    }    

    
Running on OpenShift
--------------------

Create an account at https://www.openshift.com

Install the RHC client tools if you have not already done so:
    
    sudo gem install rhc
    rhc setup

Select the version of python (2.7 or 3.3) and create a application

    rhc app create django python-$VERSION

Add this upstream repo

    cd django
    git remote add upstream -m master git@github.com:kleiberjp/zoe-developer-test.git
    git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

Now, you have to create [admin account](#admin-user-name-and-password), so you 
can setup your Django instance.
	
That's it. You can now checkout your application at:

    http://django-$yournamespace.rhcloud.com

Admin user name and password
----------------------------
Use `rhc ssh` to log into python gear and run this command:

	python $OPENSHIFT_REPO_DIR/wsgi/myproject/manage.py createsuperuser

You should be now able to login at:

	http://$yournamespace.rhcloud.com/admin/

Project test Zoe Full Stack Developer
-------------------------------------

This is the structure of the project

    wsgi                        /*----- root path -------*/
        /apps                   /*----- path apps that contain MVC for each one models data -------*/
            ../admin.py         /*----- file that contains register for admin manager -----*/
            ../forms.py         /*----- file that contains forms for use at views app ----*/
            ../models.py        /*----- file that connect data model with models sql -----*/
            ../urls.py          /*----- url for consult REST and Views apps -----*/
            ../views.py         /*----- all views avaliable for access to data -------*/
            ../serializers.py   /*----- files for procces data json with model and views -----*/
        /project                /*---- Path for files settings app project ----*/
            settings.py
            urls.py
            wsgi.py
        /static                 /*---- Path for statics files access to client view
            css/
            img/
            js/
            
        /templates              /*---- Template for views response at app client -----*/
        application.py          /*---- file for set enviroment apps on context ------*/
        manage.py               /*---- file for django settings run app -------*/
    setup.py 
    
    
Library used in project
-------------------------------------

   * psycopg2
        
        Library for conection with database postgresql
        
   
   * djangorestframework
        
        Library for serialize model data and sent response to template in json mode for best aproach of datam in aspects of size
        and time for response
        
   * requests
   
        Library that provide flexible request parsing that allows you to treat requests with JSON data or other media types in 
        the same way that you would normally deal with form data
        
        
        