from django.utils import timezone
from django.shortcuts import get_object_or_404, render

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from gen.models import *
from django.contrib.auth.models import User

# TODO

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class HomeView(generic.ListView):
    user = User
    template_name = "gen/home.html"


@method_decorator(login_required, name='dispatch')
class HomeView(generic.ListView):
    user = User
    template_name = "gen/home.html"

@method_decorator(login_required, name='dispatch')
class CharactersView(generic.DetailView):
    user = User
    template_name = "gen/characters.html"

@method_decorator(login_required, name='dispatch')
class StoryView(generic.DetailView):
    user = User
    template_name = "gen/story.html"

@method_decorator(login_required, name='dispatch')
class SegmentsView(generic.ListView):
    user = User
    story = Story
    template_name = "gen/segments.html"

@method_decorator(login_required, name='dispatch')
class ImagesView(generic.ListView):
    user = User
    story = Story
    template_name = "gen/images.html"

@method_decorator(login_required, name='dispatch')
class WebtoonView(generic.ListView):
    user = User
    template_name = "gen/webtoon.html"
