from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views
app_name = "gen"
urlpatterns = [
    path("", views.home, name="home"),
    path("input/", views.input, name="input"), # get user input
    path("story/", views.story, name="story"), # for viewing stories
    path("segments/", views.segments, name="segments"), # for viewing story segments
    path("images/", views.images, name="images"), # for viewing story images
    path("webtoon/", views.webtoon, name="webtoon"), # for viewing final webtoon
]