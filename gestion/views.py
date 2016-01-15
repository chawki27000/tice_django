# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from gestion.forms import ConnexionForm


def home(request):
    text = """<h1>Bienvenue sur mon site !</h1>
              <p>ça sera la page d'acceuil (pour bientot)</p>"""
    return HttpResponse(text)


# C'EST LA PARTIE ESSAI ET DEVELOPPEMENT
def connexion(request):
    error = False

    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else:  # sinon une erreur sera affichée
                error = True

    else:
        form = ConnexionForm()

    return render(request, 'gestion/connexion.html', locals())