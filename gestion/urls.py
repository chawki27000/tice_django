from django.conf.urls import patterns, url, include
from django.views.generic import ListView, TemplateView

from gestion import views
from gestion.models import Administrateur

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^connexion$', views.connexion, name='connexion')

]