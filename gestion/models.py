# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Classe ORM Administrateur
class Administrateur(models.Model):
    # id : cle primaire est mise a jour automatiquement
    """
    les informations sur le profil utilisateur est contenu dans user
    voici les information que user peut prendre :
    username : login utilisateur / login_util
    first_name : prenom utilsateur / prenom_util
    last_name : nom utilsateur / nom_util
    email : email utilisateur / mail_util
    password : mot de passe utilisateur / password_util
    last_login : date de la derniere connexion
    date_joined : date de la premiere connexion
    """
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    grade_util = models.CharField(max_length=50)

    def __str__(self):
        return self.user.last_name


# Classe ORM Formateur
class Formateur(models.Model):
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    spec_formation = models.CharField(max_length=80)
    type_formation = models.CharField(max_length=80)

    def __str__(self):
        return self.user.last_name


# Classe ORM Categorie
class Categorie(models.Model):
    lib_categ = models.CharField(max_length=200)
    administrateur = models.ForeignKey('Administrateur')

    def __str__(self):
        return self.lib_categ


# Classe ORM Formation
class Formation(models.Model):
    lib_form = models.CharField(max_length=80)
    date_deb_form = models.DateField(auto_now=False, auto_now_add=False)
    date_fin_form = models.DateField(auto_now=False, auto_now_add=False)
    categorie = models.ForeignKey('Categorie')

    def __str__(self):
        return self.lib_form


# Classe ORM Apprenant
class Apprenant(models.Model):
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    grade_util = models.CharField(max_length=50)
    diplome_appr = models.CharField(max_length=80)
    formation = models.ForeignKey('Formation')

    def __str__(self):
        return self.user.last_name


# Classe ORM Regroupement
class Regroupement(models.Model):
    date_group = models.DateField(auto_now=False, auto_now_add=False)
    formation = models.ForeignKey('Formation')

    def __str__(self):
        return str(self.formation)


# Classe ORM Cours
class Cours(models.Model):
    lib_cour = models.CharField(max_length=80)
    formation = models.ForeignKey('Formation')

    def __str__(self):
        return self.lib_cour


# Classe ORM Chapitre
class Chapitre(models.Model):
    lib_chap = models.CharField(max_length=80)
    cours = models.ForeignKey('Cours')

    def __str__(self):
        return self.lib_chap


# Classe ORM Ressource
class Ressource(models.Model):
    lib_ress = models.CharField(max_length=80)
    type_ress = models.CharField(max_length=50)
    chapitre = models.ForeignKey('Chapitre')

    def __str__(self):
        return self.lib_ress


# Classe ORM Animer
class Animer(models.Model):
    id_util = models.ForeignKey('Formateur')
    id_form = models.ForeignKey('Formation')

    def __str__(self):
        return str(self.id_util)


# Classe ORM Test
class Test(models.Model):
    id_util = models.ForeignKey('Apprenant')
    id_form = models.ForeignKey('Formation')

    date_test = models.DateField(auto_now=False, auto_now_add=False)
    note_test = models.IntegerField()

    def __str__(self):
        return str(self.date_test)
