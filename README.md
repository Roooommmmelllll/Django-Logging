# Django-Logging #
A set of the Django experiments I've done/ am working on involving logging

## Creating Projects
- My first realization is that the Django platform is not very friendly on Windows, so I loaded up a linux virtual machine, and contued to do all my further work on that.

- Command Line Input:

		 django-admin startproject projecttitle

  * In my actual work, I followed direction verbatim, in which I called the project "mysite"
- This command will start a django project folder within the folder where the command was inputted
- The folder will be given the project title name and a file called "manage.py" wchich will be heavily used later
  * There is another same-named folder containing many files oriented to how the django project will be built
  * Some of the files included in this folder will be modified in the building of the django project

## Modifying "settings.py"

- In the subfolder titled "mysite", exists a file called "settings.py"
- This will be modified to the needs of the project
- Note that intitially, settings.py is set to handle SQLite databases, and is defualt to that.
- Luckily, I was informed that the project we're involved in also uses SQLite
- Open the settings.py file in some sort of text editing software, such as "vi" or "emacs".
  * Scroll down to the section that looks like:
  
    		DATABASES = {
           		'default':{
                 'ENGINE':'django.db.backends.sqlite3',
                 'NAME':os.path.join(BASE_DIR, 'databasename'),
           		}
     		}
  * In my experimenting, the databasename is set to "ex1"
  * By default, the directory for the project's database building will be the same as the prject itself
- Immediately below this section contains settings for language and time zone, modify as necessary
- Navigate to the top of the file to find the "INSTALLED_APPS" seciton.
- This will be modified by later work, but for now, know that this area stores the list of all apps to be loaded when the django project is initialized.
- Some of the default apps are not necessary, so, modify as needed.

**DO NOT FORGET TO SAVE AND CLOSE THE FILE**

## Initializing Server

- Command Line Input:

    	python manage.py migrate

- This command looksa at 'settings.py', specifically at "INSTALLED_APPS", as well as any database tables required to be built.

## Starting Server

- Command Line Input:

		python manage.py runserver

  * This command starts the srver after any initial self-testing and is now ready for Django development

- By defualt, the server will be run on Port 8000 and on the same IP address

- This can be changed simply by adding an ip and port after the command, like "python manage.py runserver 0.0.0.0:8001"

- The server can then be shutdown, as is shown in the command prompt, with *ctrl + c*

## Creating Apps

- Command Line Input:

		python manage.py statapp appname

- Creates a directory with the desired appname
- For the example the instructions that I am following will use "polls"

## Creating Models

- Within the polls folder created, exists a file called "models.py"
- Open this file for editing:
	* All models are in the form of classes
	* For example:
	
			class Question(models.Model):
				question = models.CharField(max_length=200)
				pub_date = models.Datetimefield('date published')

- All model creation is very straightforward, and is a sublass of **django.db.models.Model**
- All instances of the class are an instance of a **Field** class; this tells Django what type of data each field holds

## Activating Apps
- Once models are created in the "models.py" file, they tell Django a lot, but the app they are a part of must first be activated.
- Open the file "settings.py" again for editing
	* You must add the app you created to the line of other installed apps to be run by Django
	* The section will look something like:
		
			INSTALLED_APPS = (
				'django.contrib.admin',
				'django.contrib.auth',
			    'django.contrib.contenttypes',
			    'django.contrib.sessions',
			    'django.contrib.messages',
			    'django.contrib.staticfiles',
			    'polls',
			)

- There is an important command that must be run in order to tell Django that there were changes made to your models.
	* This also applies to any new models created.
- Command Line Input:
	
		python manage.py makemigrations appname
	* In my example, I created an app called "polls", so the command would look like:
		
			python manage.py makemigrations polls
- Once the makemigrate has been run, you must once again initialize the changes onto the server
- Command Line Input:
		
		python manage.py migrate
- Summary:
	* When changes in the models (models.py)
	* Run **makemigrations** to create the migrations for those changes
	* Run **migrate** to apply those changes to the database

**SKIPPING SOME UNNECESSARY FEATURES**

## Writing Forms