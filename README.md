
# Environment create & activate
1. Create a Virtual Environment
- python -m venv venv

2. Activate the Virtual Environment
In Window
- .\venv\Scripts\activate
In Powershell
- .\venv\Scripts\Activate.ps1
In macOs/Linux 
- source venv/bin/activate

# Install Django and create project 
3. Install Django 
- pip install django

4. To view the installed version of django
- python -m django --version

5. Create any folder locally
- Eg. django-project

6. Go to that folder path and enter below command to view the command list.
- django> django-admin

7. To create the new project run below command
- django-admin startproject <your_new_project_name> eg. mysite

- Folder structure
- mysite --> directory (we can change the directory name)
	<pre>
	|mysite
	├── manage.py
	├── project1/
	│   ├── settings.py
	│   ├── urls.py
	│   ├── __init__.py
	│   ├── asgi.py.py
	│   ├── ...
	</pre>

8. To run the project 
- django/mysite/mysite> python manage.py runserver
(Note : Which give us a one server with IP like http://127.0.0.0:8000)


# Our First Django Website
9. Create the views.py file ander mysite folder
- views.py

10. Simple code to create function and access it from urls.py file
from django.http import HttpResponse
def index(request):
<pre>return HttpResponse("<h1>Hello World</h1>")</pre>

def about(request):
<pre>return HttpResponse("<h1>About Us page</h1>")</pre>

11. Open urls.py file and create the url
from django.urls import path
from .import views

urlpatterns = [
path('admin/',admin.site.urls),
path('',views.index, name="index"),
path('about-us/',views.about,name="about")
]

12. Run server and enter url 
	http://127.00.00/8000
	http://127.00.00/8000/about-us

# Django Templates
- Go to settings.py
- Find 'DIRS': [] in TEMPLATES json object
- Add 'templates' inside DIRS['templates] --> it is the our template folder
- Create the 'template' folder parallel to manage.py and create in that index.html file
  <ul>
	<li>templates</li>
	<ul>
		<li>index.html</li>
		<li>aboutus.html</li>
	</ul>
  </ul>
- Open views.py file and add 
  - from django.shortcuts import render
  - def index(request):
    return render("index.html")

# To display the image from project
project/
<pre>
├── manage.py
├── project1/
│   ├── settings.py
│   ├── urls.py
│   ├── ...
├── static/
│   ├── bandmember.jpg
├── templates/
│   ├── index.html
</pre>
1. Open settings.py
2. <pre>
	STATIC_URL = 'static/'
	STATICFILES_DIRS = [
		os.path.join(BASE_DIR, "static"),
	]
	STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
	</pre>
3. Create the static folder inside project1 <your project name>
4. Add image there or add with create folder. eg. abc.jpg
5. Go to your html file add line to starting of html 
   - {% load static %}
   - <img src="{% static 'abc.jpg' %}">
