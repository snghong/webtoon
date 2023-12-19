from django.utils import timezone
from django.shortcuts import get_object_or_404, render

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from gen.forms import WebtoonForm
from gen.models import *
from django.contrib.auth.models import User

# TODO

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

def home(request):
    context = {}
    return render(request, "gen/home.html", context)


# take user input for characters and context, then generate story
def input(request):
    context = {}
    return render(request, "gen/input.html", context)

# user form POST endpoint
def get_details(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = WebtoonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Using the data from form.cleaned_data:

            # TODO: 1. save the user's characters and context in the database

            # TODO: 2. call text gen API and save the user's story in the database

            # redirect to show story
            return render(request, "gen/story.html", {})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WebtoonForm()
    return render(request, "gen/characters.html", {"form": form})
# display story
def story(request):
    context = {}
    return render(request, "gen/story.html", context)

def segments(request):
    context = {}
    return render(request, "gen/segments.html", context)

def images(request):
    context = {}
    return render(request, "gen/images.html", context)

def webtoon(request):
    context = {}
    return render(request, "gen/webtoon.html", context)

