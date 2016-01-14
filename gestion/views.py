# -*- coding: utf-8 -*-
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView

from gestion.models import Administrateur


def home(request):
    text = """<h1>Bienvenue sur mon site !</h1>
              <p>ça sera la page d'acceuil (pour bientot)</p>"""
    return HttpResponse(text)


# C'EST LA PARTIE ESSAI ET DEVELOPPEMENT
def lire(request, id):

    admin1 = Administrateur.objects.filter(id=id)
    return render(request, 'gestion/info.html', locals())

class ListeAdmin(ListView):
    model = Administrateur
    context_object_name = "derniers_admin"
    template_name = "gestion/affichage.html"
    paginate_by = 5
