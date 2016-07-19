//*--- Kleiber J Perez --*//
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
    setup.py                    /*---- file that contains required libraries and name app ----*/    
        
            