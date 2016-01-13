from django.conf.urls import url, patterns
from gestion import views

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'demande/(?P<id>\d+)$', views.view_demande),
    url(r'^redirection$', views.view_redirection),
    url(r'^date$', views.date_actuelle),
    url(r'^affichage/(?P<id>\d+)$', views.affichage),
]