# -*- coding: utf-8 -*-
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from gestion.forms import AdministrateurForm, FormateurForm, CategorieForm
from gestion.forms import FormationForm, ApprenantForm, RegroupementForm
from gestion.forms import CoursForm, ChapitreForm, RessourceForm, AnimerForm, TestForm


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


def apprenant(request):
    if request.method == 'POST':
        form = ApprenantForm(request.POST)

        if form.is_valid():
            a = 1

    else:
        form = ApprenantForm()

    return render(request, 'gestion/form_appre.html', locals())


def regroupement(request):
    if request.method == 'POST':
        form = RegroupementForm(request.POST)

        if form.is_valid():
            a = 1

    else:
        form = RegroupementForm()

    return render(request, 'gestion/form_regroup.html', locals())


def cours(request):
    if request.method == 'POST':
        form = CoursForm(request.POST)

        if form.is_valid():
            a = 1

    else:
        form = CoursForm()

    return render(request, 'gestion/form_cours.html', locals())


def chapitre(request):
    if request.method == 'POST':
        form = ChapitreForm(request.POST)

        if form.is_valid():
            a = 1

    else:
        form = ChapitreForm

    return render(request, 'gestion/form_chapitre.html', locals())


def ressource(request):
    if request.method == 'POST':
        form = RessourceForm(request.POST)

        if form.is_valid():
            a = 1

    else:
        form = RessourceForm()

    return render(request, 'gestion/form_ress.html', locals())


def animer(request):
    if request.method == 'POST':
        form = AnimerForm(request.POST)

        if form.is_valid():
            a = 1

    else:
        form = AnimerForm()

    return render(request, 'gestion/form_animer.html', locals())


def test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)

        if form.is_valid():
            a = 1

    else:
        form = TestForm()

    return render(request, 'gestion/form_test.html', locals())
