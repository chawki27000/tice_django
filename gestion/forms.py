# -*- coding: utf-8 -*-
from django import forms
from models import Categorie, Formation, Apprenant, Regroupement, Cours
from models import Chapitre, Ressource, Animer, Test
from django.contrib.auth.models import User


class AdministrateurForm(forms.ModelForm):
    # username = forms.CharField(max_length=100)
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    grade_util = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]


class FormateurForm(forms.ModelForm):
    # username = forms.CharField(max_length=100)
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    spec_formation = forms.CharField(max_length=80)
    type_formation = forms.CharField(max_length=80)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = [
            "lib_categ",
            "administrateur",
        ]


class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = [
            "lib_form",
            "date_deb_form",
            "date_fin_form",
            "categorie",
        ]


class ApprenantForm(forms.ModelForm):
    class Meta:
        model = Apprenant
        fields = [
            "user",
            "grade_util",
            "diplome_appr",
            "formation",
        ]


class RegroupementForm(forms.ModelForm):
    class Meta:
        model = Regroupement
        fields = [
            "date_group",
            "formation",
        ]


class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = [
            "lib_cour",
            "formation",
        ]


class ChapitreForm(forms.ModelForm):
    class Meta:
        model = Chapitre
        fields = [
            "lib_chap",
            "cours",
        ]


class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = [
            "lib_ress",
            "type_ress",
            "chapitre",
        ]


class AnimerForm(forms.ModelForm):
    class Meta:
        model = Animer
        fields = [
            "id_util",
            "id_form",
        ]


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [
            "id_util",
            "id_form",
            "date_test",
            "note_test",
        ]
