# chat_project/urls.py

from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = "tools"

urlpatterns = [
    path('generate_response/', generate_response, name='generate_response'),  # Handle AJAX requests
    path('', fetch_images, name='fetch_image'),  # Handle AJAX requests


]
