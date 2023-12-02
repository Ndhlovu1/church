from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
    
"""DOCUMENTATION TAGS

1. Go into the Project Folder(ChurchProject)
2. Go into the urls.py folder
3. Edit the urls.py and include the index function into the Project urls.py file

"""

def index(request):
    #greeting = "Welcome to My Django App"
    return render(request, "blog/index.html")

#Create a description view
def about(request):
    title = "<center> <h1 style='color:tomato;'> Django Blog </h1>"

    return HttpResponse(title)




