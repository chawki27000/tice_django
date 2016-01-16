from django.conf.urls import patterns, url, include
from django.views.generic import ListView, TemplateView

from gestion import views
from gestion.models import Administrateur

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^forms/admin$', views.administrateur),
    url(r'^forms/formateur', views.formateur),
    url(r'^forms/categorie', views.categorie),
    url(r'^forms/formation', views.formation),

]