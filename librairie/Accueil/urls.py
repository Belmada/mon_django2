
from django.urls import path

from . import views

app_name = "Accueil"   

urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.register_request, name="register"),
]