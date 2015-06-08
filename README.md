# Django-Logging #
A set of the Django experiments I've done/ am working on involving logging

## Creating Projects
- My first realization is that the Django platform is not very friendly on Windows, so I loaded up a Linux virtual machine, and continued to do all my further work on that.

- Command Line Input:

		 django-admin startproject projecttitle

  * In my actual work, I followed direction verbatim, in which I called the project "mysite"
- This command will start a Django project folder within the folder where the command was inputted
- The folder will be given the project title name and a file called "manage.py" wchich will be heavily used later
  * There is another same-named folder containing many files oriented to how the Django project will be built
  * Some of the files included in this folder will be modified in the building of the Django project

## Modifying "settings.py"

- In the sub-folder titled "mysite", exists a file called **"settings.py"**
- This will be modified to the needs of the project
- Note that initially, settings.py is set to handle SQLite databases, and is default to that.
- Luckily, I was informed that the project we're involved in also uses SQLite
- Open the **"settings.py"** file in some sort of text editing software, such as "vi" or "emacs".
  * Scroll down to the section that looks like:
  
    		DATABASES = {
           		'default':{
                 'ENGINE':'django.db.backends.sqlite3',
                 'NAME':os.path.join(BASE_DIR, 'databasename'),
           		}
     		}
  * In my experimenting, the database name is set to "ex1"
  * By default, the directory for the project's database building will be the same as the project itself
- Immediately below this section contains settings for language and time zone, modify as necessary
- Navigate to the top of the file to find the "INSTALLED_APPS" section.
- This will be modified by later work, but for now, know that this area stores the list of all apps to be loaded when the Django project is initialized.
- Some of the default apps are not necessary, so, modify as needed.

**DO NOT FORGET TO SAVE AND CLOSE THE FILE**

## Initializing Server

- Command Line Input:

    	python manage.py migrate

- This command looks at **"settings.py"**, specifically at "INSTALLED_APPS", as well as any database tables required to be built.

## Starting Server

- Command Line Input:

		python manage.py runserver

  * This command starts the server after any initial self-testing and is now ready for Django development

- By default, the server will be run on Port 8000 and on the same IP address

- This can be changed simply by adding an IP and port after the command, like:
	
		python manage.py runserver 0.0.0.0:8001

- The server can then be shutdown, as is shown in the command prompt, with *ctrl + c*

## Creating Apps

- Command Line Input:

		python manage.py statapp appname

- Creates a directory with the desired app name
- For the example the instructions that I am following will use "polls"

## Creating Models

- Within the polls folder created, exists a file called **"models.py"**
- Open this file for editing:
	* All models are in the form of classes
	* For example:
	
			class Question(models.Model):
				question = models.CharField(max_length=200)
				pub_date = models.Datetimefield('date published')

- All model creation is very straightforward, and is a subclass of **django.db.models.Model**
- All instances of the class are an instance of a **Field** class; this tells Django what type of data each field holds

## Activating Apps
- Once models are created in the **"models.py"** file, they tell Django a lot, but the app they are a part of must first be activated.
- Open the file **"settings.py"** again for editing
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
- Once **"makemigrations"** has been run, you must once again initialize the changes onto the server
- Command Line Input:
		
		python manage.py migrate
- *Summary*:
	* When changes are made in the models (models.py):
	* Run **"makemigrations"** to create the migrations for those changes
	* Run **"migrate"** to apply those changes to the database

**SKIPPING SOME UNNECESSARY FEATURES**

## Creating Views

- Using the example I've used, open the **"views.py"** file in the polls folder
- Edit the **"polls/views.py"** file so that it looks like

		from django.http import HttpResponse
		
		def index(reqeust):
			return HttpResponse("Hello, world. You're at the polls index.")
		
		def detail(request, question_id):
			return HttpResponse("You're looking at question %s." % question_id)

		def results(request, question_id):
			response = "You're looking at the results of question %s"
			return HttpResponse(response % question_id)

		def vote(request, question_id):
			return HttpResponse("You're voting on question %s" % question_id)
- The **"views.py"** file is used to store all page request responses for different pages on the site created by Django
- In this example, the index is simply what we're calling the "view" of the site that is the main screen.

## Creating urls.py
- Inside the app's main folder, in my example, "polls", you must create a new file to store all url calls.
- This file will have all calls linked to specific views in the views.py file edited just before this section.
- Edit the **polls/urls.py** file so that it looks like:

		from django.conf.urls import url

		from . import views

		urlpatterns = [
			# ex: /polls/
			url(r'^$', views.index, name='index'),
			# ex: /polls/1/
			url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
			# ex: /polls/1/results/
			url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
			# ex: /polls/1/vote/
			url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
		]
- This is easily explained; the "urlpatterns" stores all URL endings that the app will use, as well as what view they are connected to.
	* Index is just a simple way to name the main page for the polls app
	* the sections that include question id will display whatever is used for the URL in the call to the corresponding view
- Now we must create the URL links for the main site.
- Edit the **"mysite/urls.py"** file to look like:
		
		from django.conf.urls import include, url
		from django.contrib import admin
	
		urlpatterns = [
			url(r'^polls/', include('polls.urls')),
			url(r'^admin/', include(admin.site.urls)),
		]
- This part is a little more involved than the previous urls.py
	* Mainly because it doesn't create its own URLs, but includes the ones that already exist.

## Using Templates
- The template directory, by default, does not exist, so create it within the app folder, in my example, polls.
- When the Django server runs, it will look for templates within this folder.
	* Within this new folder "templates" you must create another folder with the same name as your app, in my example, polls.
	* Then within that new folder, create a new file called index.html
	* In other words, the directory should look like:
		* appname/templates/appname/index.html
	* Or in my example:
		*  polls/templates/polls/index.html
- Now to edit that template.
- Edit the **"polls/templates/polls/index.html"** file to look like this:

		{% if latest_question_list %}
			<ul>
			{% for question in latest_question_list %}
				<li><a href="/polls/{{ question_id }}/">{{ question.question_text }}</a></li>
			{% endfor %}
			</ul>
		{% else %}
			<p>No polls are available.</p>
		{% endif %}
- I'm sure it was obvious that the file is an html file, and is formatted as such.
- There is also some python code in the formatting surrounded in {% code %}
- Now to reconfigure the views file so that is uses this new template.
- **NOTE : These changes will alter the *views.py* previously written into.**
- Edit the **"polls/views.py"** to look like:

		from django.http import HttpResponse
		from django.template import RequestContext, loader

		from .models import Question

		def index(request):
			latest_question_list = Question.objects.order_by('-pub_date')[:5]
			template = loader.get_template('polls/index.html')
			context = RequestContext(request, {'latest_question_list':latest_quesiton_list,})
			return HttpResponse(template.render(context))
- But now that you've seen what it looks like to load a template, fill a context, and return a HttpResponse object of the rendered template, know that it can be done in an easier way. Django has shortcuts built to make life easier.
- Edit the **"polls/views.py"** to look like:

		from django.shortcuts import render
		from django.http import HttpResponse

		from .models import Question

		def index(request):
			latest_question_list = Question.objects.order_by('-pub_date')[:5]
			context = {'latest_question_list':latest_question_list,})
			return render(request, 'polls/index.html', context)
		#...
- The changes made simplify how requests are handled that involve templates.
- Now to include the question detail view for the poll example, and introduce the 404 Error syntax.
- Edit the **"polls/views.py"** to add:
		
		from django.shortcuts import render
		from django.http import HttpResponse, Http404

		from .models import Question
		#...
		def detail(request, question_id):
			try:
				question = Question.objects.get(pk=question_id)
			except Question.DoesNotExit:
				raise Http404("Question does not exist")
			return render(request, 'polls/detail.html', {'question': question})
- But again, now  that you've seen the more difficult method, know that Django has a shortcut for 404 Errors.
- Edit the **"polls/views.py"** to now show:

		from django.shortcuts import render, get_object_or_404
		from django.http import HttpResponse

		from .models import Question
		#...
		def detail(request, question_id):
			question = get_object_or_404(Question, pk=question_id)
			return render(request, 'polls/detail.html', {'question': question})
- Now that there is a setup for the Question detail in **"views.py"**, we can create the template for it.
- Create a file within the templates.polls folder called **"detail.html"**.
- Edit the **"polls/templates/polls/detail.html"** file to look like:

		<h1>{{ question.question_text }}</h1>
		<ul>
		{% for choice in question.choice_set.all %}
			<li>{{ choice.choice_text }}</li>
		{% endfor %}
		</ul>
- While we're editing template files, there is a formatting change we can make to the index file from earlier.
- Since our URL files use the **"name='somename' "** convention, we can use that to link to templates instead of hardcoded URLs.
- Edit the **"polls/templates/polls/index.html"** file to now use the **{% url %}** template tag:

		{% if latest_question_list %}
			<ul>
			{% for question in latest_question_list %}
				<li><a href="{% url 'detail' question_id %}">{{ question.question_text }}</a></li>
			{% endfor %}
			</ul>
		{% else %}
			<p>No polls are available.</p>
		{% endif %}
- Now instead of looking for the specific URL, it will now search for the given URL-name defined in the **"views.py file"**
- One last section for templates involve a **"namespace"** used to differentiate URL names in projects with a multitude of apps.
- Edit the **"mysite/urls.py"** file to now look like:
		
		from django.conf.urls import include, url
		from django.contrib import admin

		urlpatterns = [
			url(r'^polls/', include('polls.urls', namespace ="polls")),
			url(r'^admin/', include(admin.site.urls)),
		]
- This also involves changing the html file for the corresponding template files.
- Edit the **"polls/templates/polls/index.html"** file to now use the namespaced detail view:

		{% if latest_question_list %}
			<ul>
			{% for question in latest_question_list %}
				<li><a href="{% url 'polls:detail' question_id %}">{{ question.question_text }}</a></li>
			{% endfor %}
			</ul>
		{% else %}
			<p>No polls are available.</p>
		{% endif %}
## Creating Forms