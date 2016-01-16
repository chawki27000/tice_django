# -*- coding: utf-8 -*-
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from gestion.forms import AdministrateurForm, FormateurForm, CategorieForm
from gestion.forms import FormationForm


def home(request):
    text = """<h1>Bienvenue sur mon site !</h1>
              <p>ça sera la page d'acceuil (pour bientot)</p>"""
    return HttpResponse(text)


def administrateur(request):
    if request.method == 'POST':
        form = AdministrateurForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            grade_util = form.cleaned_data['grade_util']

            # faire une entrée dans la base de données

    else:
        form = AdministrateurForm()

    return render(request, 'gestion/form_admin.html', locals())


def formateur(request):
    if request.method == 'POST':
        form = FormateurForm(request.POST)

        if form.is_valid():
            a = 1

    else:
        form = FormateurForm()

    return render(request, 'gestion/form_formateur.html', locals())


def categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)

        if form.is_valid():
            a = 1

    else:
        form = CategorieForm()

    return render(request, 'gestion/form_categorie.html', locals())


def formation(request):
    if request.method == 'POST':
        form = FormationForm(request.POST)

        if form.is_valid():
            a = 1

    else:
        form = FormationForm()

    return render(request, 'gestion/form_formation.html', locals())
