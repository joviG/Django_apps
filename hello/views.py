from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def vitalii(request):
    return HttpResponse("Hello, Vitalii!")

def david(request):
    return HttpResponse("Hello, David!")

#adding a new function with a paramater that takes someones name
def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")

    #when you render the template 'hello/greet.html' you provide that with an additional info
    #such as a dictionary down here (key of "name") - giving that template access to a variable called name
    #also that name down below is an argument to the func greet
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })