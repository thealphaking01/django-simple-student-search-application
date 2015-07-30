isntall djnago

install python-mysqldb

install mysql



in folder mysite, edit settings.py and edit the following things-

1. Name of the database
2. User of the database
3. Password of the user
4. Edit the template directory present in TEMPLATE_DIRS to where the current folder resides, accordingly
4. Do the same with STATICFILES_DIRS 


 Go to the root directory of the project and run the command python manage.py syncdb from the terminal. Create a super user as prompted.
 Now run python manage.py runserver from the terminal.
 The site is live! go to http://127.0.0.1:8000/admin for entering details in the database( this can also be done by parsing the escel doc using python)
 go to http://127.0.0.1:8000/ for the app
