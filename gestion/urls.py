from django.conf.urls import url

from gestion import views

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^date$', views.date),
    url(r'^forms/admin$', views.administrateur),
    url(r'^forms/formateur', views.formateur),
    url(r'^forms/categorie', views.categorie),
    url(r'^forms/formation', views.formation),
    url(r'^forms/apprenant', views.apprenant),
    url(r'^forms/regroup', views.regroupement),
    url(r'^forms/cours', views.cours),
    url(r'^forms/chapitre', views.chapitre),
    url(r'^forms/ress', views.ressource),
    url(r'^forms/animer', views.animer),
    url(r'^forms/test', views.test),

]