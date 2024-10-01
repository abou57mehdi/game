# game/urls.py
from django.urls import path
from . import views

app_name = 'game'  # Define the app name for namespacing

urlpatterns = [
    path('', views.password_game, name='password_game'),
    # Other URL patterns...
]
