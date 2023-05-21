from django.urls import path
from . import views

# Url Configuration (URLConf)
urlpatterns = [
    path('hello', views.say_hello)
]