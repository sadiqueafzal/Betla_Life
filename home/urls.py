from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("tour", views.tour, name='tour'),
    path("map", views.map, name='map'),
    path("gallery", views.gallery, name='gallery'),

]