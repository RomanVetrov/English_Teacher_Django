from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("life/", views.life),
    path("contacts/", views.contacts)
]