from django.urls import path
from . import views

urlpatterns = [
    path("harold/", views.harold, name="harold"),
]
