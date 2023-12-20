from django.utils import timezone
from django.shortcuts import get_object_or_404, render

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from gen.forms import WebtoonForm
from gen.models import *
from django.contrib.auth.models import User

from gen.ai import get_ai_generated_story

# TODO

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

def home(request):
    context = {}
    return render(request, "gen/home.html", context)


# take user input for characters and context, then generate story
# user form POST endpoint
def input(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        print("received POST request")
        # create a form instance and populate it with data from the request:
        form = WebtoonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Using the data from form.cleaned_data:
            # TODO: see if we want to add other fields like genre
            location = form.cleaned_data['location']
            details = form.cleaned_data['details']
            character1name = form.cleaned_data['character1name']
            character1details = form.cleaned_data['character1details']
            character2name = form.cleaned_data['character2name']
            character2details = form.cleaned_data['character2details']

            # save the user's characters and context in the database
            user = request.user
            user.save()
            context = Context(location = location, user = user, details = details)
            character1 = Character(user = user, name = character1name, details = character1details)
            character2 = Character(user = user, name = character2name, details = character2details)
            context.save()
            character1.save()
            character2.save()

            # call text gen API
            ai_story = get_ai_generated_story(location, details, character1name, character1details,
                                                   character2name, character2details)
            story = Story(user = user , title = "webtoon", text = ai_story)

            # save generated story to database
            story.save()
            # redirect to show story
            return render(request, "gen/story.html", {'story': ai_story})
        else:
            print(f"FORM ERRORS: {form.errors}")
            print("form was not valid...")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = WebtoonForm()
    return render(request, "gen/input.html", {"form": form})

# display story
def story(request):
    context = {'story': request.user.story}
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

