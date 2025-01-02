# Self created views.py file
# Here we create the functions

from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
    #return HttpResponse("<h1>Home Page</h1>")

def index(request):
    return render(request,"index.html")