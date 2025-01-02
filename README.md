
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
<ul>
	<li>
		mysite
		<ul>
			<li>__phcache__ folder</li>
			<li>__init__.py</li>
			<li>asgi.py</li>
			<li>settings.py</li>
			<li>urls.py</li>
			<li>wsgi.py</li>
		</ul>
	</li>
	<li>manage.py</li>
	<li>db.sqlite3</li>
</ul>
|__mysite --> our project name
|   |___init__.py
|   |___asgi.py
|   |___settings.py  
|   |___urls.py      ----> We can add here our urls
|   |___wsgi.py
|
|__manage.py --> Utility file which help us to intract with django project

8. To run the project 
- django/mysite/mysite> python manage.py runserver
(Note : Which give us a one server with IP like http://127.0.0.0:8000)


# Our First Django Website
9. Create the views.py file ander mysite folder
- views.py

10. Simple code to create function and access it from urls.py file
from django.http import HttpResponse
def index(request):
- return HttpResponse("<h1>Hello World</h1>")

def about(request):
- return HttpResponse("<h1>About Us page</h1>")

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
