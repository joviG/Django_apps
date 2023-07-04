from django.urls import path

from . import views

urlpatterns = [
    #default route. represented by the empty string. 
    #that loads the index function
    path("", views.index, name="index"),

    #here could be any string to give a variable name of 'name'
    #then it calls the greet function
    #when that func is called. it will pass in this arg, (this <name>) as a parameter to that function 
    path("<str:name>", views.greet, name="greet"),

    path("vitalii", views.vitalii, name="vitalii"),
    #path("a URL (what comes after the /hello)")
    #then there is a functino to run, the david function inside of views.py
    #then giving it a name to easy reference a bit later
    path("david", views.david, name="david")
]