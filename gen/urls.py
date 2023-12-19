from django.urls import include, path

from . import views
app_name = "gen"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("characters/", views.CharactersView.as_view(), name="characters"), # for adding characters 
    path("story/", views.StoryView.as_view(), name="story"), # for viewing stories
    path("segments/", views.SegmentsView.as_view(), name="segments"), # for viewing story segments
    path("images/", views.ImagesView.as_view(), name="images"), # for viewing story images
    path("webtoon/", views.WebtoonView.as_view(), name="webtoon"), # for viewing final webtoon
]