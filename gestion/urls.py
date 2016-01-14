from django.conf.urls import patterns, url, include
from django.views.generic import ListView, TemplateView

from gestion import views
from gestion.models import Administrateur

urlpatterns = [
    url(r'^$', views.ListeAdmin.as_view(), name="blog_liste"),
    url(r'^accueil$', views.home),
    url(r'^info/(?P<id>\d+)$', views.lire),

]