# Create New Project

# AIMS - 
1. CREATE AN APPLICATION                            [ X ]
2. CREATE A DATABASE MODEL USING THE ORM            [ X ]
3. CONNECT THE DATABASESE MODEL TO THE ADMIN PANEL  [ X ] 
4. STYLE THE ADMIN PANEL                            [ X ]
5. CREATING VIEWS                                   [ Y ]
6. CREATE THE URLs                              
7. CREATE THE HTML FILES TO DISPLAY THE DATA
8. STYLE THE WEB PAGES 
9. CREATING RESTAPIs DjangoRestFramework



## CREATE AN APPLICATION

```shell
python manage.py startapp app_name
```

### Connect the Application to the project

1. Go into the churchProject folder
2. Go into the settings.py file
3. Look for the name INSTALLED_APPS = [ ... ]
4. Edit the INSTALLED_APPS and add the name of the app at the bottom of the list in the INSTALLED_APPS as a string, and add a coma after the name
5. Save the file

##  CREATE A DATABASE MODEL USING  USING THE ORM

1. Go into the blogApp folder
2. Look for the file named models.py
3. Open and Edit the file to add our database model

## CONNECT THE DATABASE MODEL TO THE ADMIN PANEL

1. Go into the blogApp folder
2. Open and Edit the file named admin.py
3. Make the Migrations
4. Open the admin panel (Run the Server)
5. Add atleast three example blog articles
6. Add a custom object manager in the models.py of the app

## CREATING VIEWS  

1. Open the application folder
2. Find and open the views.py
3. Add your view into the views.py
4. Create a urls.py file in the application folder

## SIDENOTE
1. CREATE YOUR VIEW FUNCTIONS
2. CREATE A URLS.PY file in the BlogApp 
3. Include the urls.py file in the Project urls.py file
4. Create a templates folder to hold the html files


