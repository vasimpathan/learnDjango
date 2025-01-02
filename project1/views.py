# Self created views.py file
# Here we create the functions

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Home Page")