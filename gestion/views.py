# -*- coding: utf-8 -*-
from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from gestion.models import Administrateur


# Create your views here.
def home(request):
    text = """<h1>Bienvenue sur mon site !</h1>
              <p>ça sera la page d'acceuil (pour bientot)</p>"""
    return HttpResponse(text)


def affichage(request, id):
    tuple = get_object_or_404(Administrateur, id=id)

    return render(request, 'gestion/affichage.html', locals())


# C'EST LA PARTIE ESSAI ET DEVELOPPEMENT
def view_demande(request, id):
    if int(id) > 100:
        return redirect(view_redirection)

    text = "Vous avez demandé le numero : {0} !".format(id)
    return HttpResponse(text)


def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")


def date_actuelle(request):
    return render(request, 'gestion/date.html', {'date': datetime.now()})
