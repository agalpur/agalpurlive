from django.contrib import admin
from django.urls import path
from agalpur import views

urlpatterns = [
    path("", views.index,name="index"),
    path("about", views.about,name="about"),
    path("events", views.events,name="events"),
]
