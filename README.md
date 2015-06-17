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
	- **"pk"** in the **".get"** command stands for and is a shortcut for Primary Key
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
- Lets build on what is already existing, and edit the template to contain an HTML **< form >** element.
- Edit the **"polls/templates/polls/detail.html"** file to use a form:

		<h1>{{ question.question_text }}</h1>
		
		{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

		<form action="{% url 'polls:vote' question.id %}" method="post">
		{% csrf_token %}
		{% for choice in question.choice_set.all %}
			<input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}"
			<label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label>
		<br />
		{% endfor %}
		<input type="submit" value="vote" />
		</form>
- A rundown of all the parts of this form.
	* This template uses radio buttons for each question choice.
	* The value for each radio button is the associated question choice's ID.
	* The POST data from each radio button submits choice=# where # is the ID of the selected choice.
	* This is the basic concept of how HTML forms work.
	* The form has 2 attributes that need to be defined: action and method.
		* The **action** attribute specifies where to send the form data when the form is submitted.
			* Normally the action attribute uses an absolute URL, pointing to some website
			* It can however, also use a relative URL, pointing to a file within the website
		* The **method** attribute is important, but can only store one of two values: get and post
			* The **get** is default, and appends the form-data to the IRL in the action attribute
			* The **post** sends the form-data fas an HTTP post transaction
	* Since the form creates a POST, that can modify data, we need to worry about Cross Site Request Forgeries.
		* Luckily, Django handles all of that by adding the template tag:
			
				{% csrf_token %}
- Now let's create a Django view that handles the submitted data and does something with it.
- Edit the **"polls/views.py"** so that the vote now looks like:
		
		from django.shortcuts import get_object_or_404, render
		from django.http import HTTPResponseRedirect, HttpResponse
		from django.core.urlresolvers import reverse

		from .models import Choice, Question

		#...
		
		def vote(request, question_id):
			p = get_object_or_404(Question, pk=question_id)
			try:
				selected_choice = p.choice_set.get(pk=request.POST['choice'])
			except (KeyError, Choice.DoesNotExist):
				# Redisplay the question voting form.
				return render(request, 'polls/detail.html',{
					'question': p,
					'error_message': "You didn't select a choice.",
				})
			else:
				selected_choice.votes += 1
				selected_choice.save()
				# Always return an HttpResponseRedirect after successfully dealing
				# with POST data. This prevents data from being posted twice if a
				# user hits the Back button.
				return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
- A rundown of the parts of the changes made to the **"polls/views.py"** file.
	* **"request.POST"** is an object that lets you access the submitted data by key name.
		* In the example, 
				
				request.POST['choice']
		* This returns the ID of the selected choice, as a string. Note that **"request.POST"** always returns a string.
	* In the case that there is no POST data provided, a **"KeyError"** will be called, and the result will be a redisplaying of the question form with an error message.
	* Note the section towards the end of the file that returns an HttpResponseRedirect.
		* This should always be done when dealing with POST data, not so much because of Django, but because it's good Web development practice.
- Now that the vote is handled, there must be the results page that it redirects to.
- Edit the **"polls/views.py"** so that the result now looks like:

		from django.shortcuts import get_object_or_404, render
		from django.http import HTTPResponseRedirect, HttpResponse
		from django.core.urlresolvers import reverse

		from .models import Choice, Question

		#...
		def results(request, question_id):
			question = get_object_or_404(Question, pk=question_id)
			return render(request, 'polls/results.html', {question': question})
- Now to create the template for this view.
- Edit the **"polls/templates/polls/results.html"** file to look like:

		<h1>{{ question.question_texxt }}</h1>

		<ul>
		{% for choice in question.choice_set.all %}
			<li>{{ choice.choice_text }} -- {{ choice.votes }} vote {{ choice.votes|pluralize }}</li>
		{% endfor %}
		</ul>

		<a href ="{% url 'polls:detail' question.id %}">Vote again?</a>
## Using Generic Views
- Since several of the views used represent common cases of basic Web Development, Django provides a shortcut for them, called the "generic views" system.
- Amend the **"polls/urls.py"** to now look like:

		from django.conf.urls import url

		from . import views

		urlpatterns = [
			# ex: /polls/
			url(r'^$', views.IndexView.as_view(), name='index'),
			# ex: /polls/1/
			url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
			# ex: /polls/1/results/
			url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
			# ex: /polls/1/vote/
			url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
		]
- Note the changes to the linked view and the changes in URL form for the second and third url pattern.
- Amend the **"polls/views.py"** to now look like:

		django.shortcuts import get_objects_or_404, render
		django.http import HttpResponseRedirect
		django.core.urlresolvers import reverse
		django.views import generic

		from .models import Choice, Question

		class IndexView(generic.ListView):
			template_name = 'polls/index.html'
			context_object_name = 'latest_question_list'

			def get_queryset(self):
				"""Return the last five published questions."""
				return Question.objects.order_by('-pub_date')[:5]
		
		class DetailView(generic.DetailView):
			model = Question
			template_name = 'polls/detail.html'

		class ResultsView(generic.DetailView):
			model = Question
			template_name = 'polls/results.html'

		def vote(request, question_id):
			#same as before, no changes.

## Logging Introduction
- Django uses Python's builtin logging module to perform system logging.
	* Python's logging module consists of four parts:
		* Loggers
		* Handlers
		* Filters
		* Formatters
- Loggers:
	* The entry point into the logging system.
	* Each logger is like a named bucket to which messages can be written for processing.
	* Each message that is written to the logger is a Log Record.
	* Each log record also has a log level indication the severity of that specific message.
	* A log record can also contain useful metadata that describes the event that is being logged.
	* This can include details such as a stack trace or an error code.
	* When a message is given to the logger, the log level of the message is compared to the log level of the logger.
	* If the log level of the message meets or exceeds the log level of the logger itself, the message will undergo further processing.
	* If it doesn't, the message will be ignored.
	* Once a logger has determined that a message needs to be processed, it is passed to the Handler.
- Handlers:
	* The handler is the engine that determines what happens to each message in a logger.
	* It describes a particular logging behavior, such as writing a message to the screen, to a file, or to a network socket.
	* Like loggers, handlers also have a log level.
	* If the log level of a log record doesn't meet or exceed the level of the handler, the handler will ignore the message.
	* A logger can have multiple handler,s and each handler can have a different log level.
	* In this way, it is  possible to provide different forms of notification depending on the importance of a message.
		* For example, you could install one handler that forwards **ERROR** and **CRITICAL** messages to a paging service, while a second handler logs all messages(including **ERROR** and **CRITICAL** messages) to a file for later analysis.
- Filters
	* Filters are used to provide additional control over which log records are passed from logger to handler
	* By default, any log message that meets log level requirements will be handled.
		* However, by installing a filter, you can place additional criteria on the logging process
			* For example, you could install a filter that only allows **ERROR** messages from a particula source to be emitted.
	* Filters can also be used to modify the logging record prior to being emitted.
		* For example, you could write a filter that downgrades **ERROR** log records to **WARNING** records if a particula set of criteria are met.
	* Filters can be installed on logger or on handlers, multiple filters can be used in a chain to perform multiple filtering actions.
- Formatters
	* Formatters are used to describe how log records are rendered as text.
	* A formatter usually consists of a Python formatting string containing LogRecord attributes;
		* However, you can also write custom formatters to implement specific formatting behavior
- The Different Log Levels:
	* DEBUG: Lowest level, showing system information for debugging purposes
	* INFO: General system information
	* WARNING: Information that describes minor problems that occur.
	* ERROR: information describing major problems that occur.
	* CRITICAL: Information describing critical problems that occur.

##Logging Code

- Remember that there are several layers to logging, which will all be covered in the following.
- Logging configuration is specified in the project's **"settings.py"** file.
- Setting up Formatters:
	* The example will use two formats:  **verbose** and **simple**.
	
			'formatters': {
				'verbose' : {
					'format' : "[%(asctimme)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
					'datefmt' : "%d/%b/%Y %H:%M:%S"
				},
				'simple' : {
					'format' : '%(levelname)s %(message)s'
				},
			},
- Setting up Filters:
	* The example will not use a filter, but this is an example of what a filter would look like:
	
			'filters': {
					'special': {
						'()': 'project.logging.SpecialFilter',
						'foo' : 'bar',
					}
				},
	* This example of a filter defines one filter, project.logging.SpecialFilter, that uses the alias 'special'
	* In this case, the argument foo will be given a value of bar when instantiating the SpecialFilter
- Setting up Handlers:
	* The following example will tell Django to log all of our output messages to a file:
	
			'handlers': {
					'file': {
						'level': 'DEBUG',
						'class': 'logging.FileHandler',
						'filename': 'mysite.log',
						'formatter': 'verbose'
					},
				},
	* **"level"** determines at what level, and above, what is to be logged.
		* This example handler is set to log anything **"DEBUG"** and higher, which actually includes all levels.
- Setting up Loggers:
	* This example will declare two loggers to be used, one for the django core and one for the application
	
			'loggers': {
					'django': {
						'handlers': ['file'],
						'propogate': True,
						'level': 'DEBUG',
					},
					'polls': {
						'handlers': ['file'],
						'level': 'DEBUG',
					},
			}
	* Make sure to replace the **"polls"** with the name of your application.
- All these parts combined, with the remaining Logging Syntax in **"settings.py"**:

		# settings.py
		LOGGING = {
		    'version': 1,
		    'disable_existing_loggers': False,
		    'formatters': {
		        'verbose': {
		            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
		            'datefmt' : "%d/%b/%Y %H:%M:%S"
		        },
		        'simple': {
		            'format': '%(levelname)s %(message)s'
		        },
		    },
		    'handlers': {
		        'file': {
		            'level': 'DEBUG',
		            'class': 'logging.FileHandler',
		            'filename': 'mysite.log',
		            'formatter': 'verbose'
		        },
		    },
		    'loggers': {
		        'django': {
		            'handlers':['file'],
		            'propagate': True,
		            'level':'DEBUG',
		        },
		        'polls': {
		            'handlers': ['file'],
		            'level': 'DEBUG',
		        },
		    }
		} 
- Now let's set up some functions in **"views.py"** that will use logging.
- Amend the **"views.py"** with the following:

		import logging
		logger = logging.getLogger(__name__)
		def myfunction():
			logger.debug("this is a debug message!")

		defmyotherfunction():
			logger.error("this is an error message!!")

##Experimenting with  Logging
- Previous sections are created mainly by following a starter guide from the Django website.
- The following will be all experimental, with not much more than the previous sections involved.
- **First**: Implement a logging environment.
	* The previous section goes into detail as to how to go about setting up a logger, and is a lot more simple than I first imagined.
- **Second**: Answer the question, "What needs to be logged?":
	* This seems to be the most important question to be answered.
	* Depending on what is being logged, there are certain aspects of Django/Python logging where it falls short of what is necessary.
- **Third**: Answer the question, "How involved is Django to the platform?":
	* I found this question to be just as important as the last. I mentioned that there are certain aspects of Django/Python logging where it just can't perform the way I wanted it to, be it my lack of know-how or *"overcomplification"*.

- In my example, I will be utilizing the **polls** app from the guide and earlier sections.
- This will also use the logger created in the logging section previously discussed.
- Similar to the example for creating functions that involve logging, you can add a logger to any python file to get data from that file.
- Now to add a function that creates logs of the data taken from the poll app.
- Open the **"views.py"** and add the following function:

		#Make sure that logging is imported
		#Make sure that the logger object is created

		import logging
		logger = logging.getLogger(__name__)

		def logdata(question_id, choice):
			logger.info(str(question_id)+"-"+str(choice))
- This is a very simple use of a logger object within a set of python code.
- The reason it is in **"views.py"** is because that file handles the voting of the polls app.
- Now to add the call into the vote view so that each vote can be logged.
- Add this call to the vote view in **"views.py"**:

		logdata(question_id, selected_choice)
- But, there is a lot more that can be added to make this logging function that much better.
- Let's add a timestamp to each log added.

		#Add this import to the top of the file
		import datetime
		#This will access a builtin python library for time
		import logging
		logger = logging.getLogger(__name__)

		#Now edit the logdata function to include this new part:
		def logdata(question_id, choice):
			logger.info(str(datetime.datetime.now())+str(question_id)+"-"+str(choice))
- This will now add a timestamp at the instant the log is created. Although, datetime is a little too accurate, and most likely you don't need the milliseconds of the log.
- A little string truncating can be added to make the logs shorter.

		def logdata(question_id, choice):
			logger.info(str(datetime.datetime.now())[:19]+"-"+str(question_id)+"-"+str(choice))

- But this isn't a lot of information for logging, we can use more.
- One thing we can add, is session information, more importantly, the session id of the user whose poll data was taken from
- Luckily, Django projects have all this already enabled.
- It's just a matter of using it within the logger, which is simpler than it sounds.
- Edit the same **"logdata"** function within **"views.py"**:

		def logdata(question_id, choice, session):
			session.modified=True
			logger.info(str(datetime.datetime.now())[:19]+"-"+str(session.session_key)+"-"+str(question_id)+"-"+str(choice))
- Note that you now need to change how the function is called, which now looks like:

		logdata(question_id, selected_choice, request.session)

- Now to explain what this all does:
	* **request.session** in the function call sends the session of the request made to the vote view.
	* **session.modified=True** edits a value in the given session to make sure that a session is created in case that it is not.
		* This part I've added due to some testing how sessions work within Django, which is cookie based by default.
		* I deleted the cookie so that I could simulate a different user logging info to the poll app.
		* And at first, the **session id = none**
		* Adding this line created a new session_id in the case that one does not exist.
	* **session.session_key** is the value of the user's session cookie id, specific to that user.