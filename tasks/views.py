from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="NewTask")

# Create your views here.
def index(request):
    if "tasks" not in request.session:   # look inside the session to see is there already a list of tasks in that session
        request.session["tasks"] = []    # if there isn't - I'd like to create the empty one

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]   #pass in that list of tasks
    })

def add(request):
    if request.method == "POST":             # checking if the user submitted some data (if the request method is POST)
        form = NewTaskForm(request.POST)     # figure out the submitted data and save it inside the variable 'form'
        if form.is_valid():                  # check if the data were provided in the right format
            task = form.cleaned_data["task"] # if so - then we get the provided ["task"]
            request.session["tasks"] += [task]     # and add it to the list of tasks that have alredy stored inside of the session before redirecting the user
            return HttpResponseRedirect(reverse("tasks:index"))   # we use reverse function (django needs to figure out the url by passed in name)
        else:                                # otherwise if it's not valid
            return render(request, "tasks/add.html", {  # we render that same html file back to user
                "form": form                            # pass in the form user has submitted (can see all of the errors made)
            })
    
    return render(request, "tasks/add.html", {  # if the request method was just GET
        "form": NewTaskForm()                   # user gets an empty form
    })