# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
# Classe ORM Administrateur
class Administrateur(models.Model):
    # id : cle primaire est mise a jour automatiquement
    nom_util = models.CharField(max_length=200)
    prenom_util = models.CharField(max_length=200)
    mail_util = models.EmailField()
    password_util = models.CharField(max_length=50)
    login_util = models.CharField(max_length=30)
    grade_util = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de creation")

    def __str__(self):
        return self.id


# Classe ORM Formateur
class Formateur(models.Model):
    nom_util = models.CharField(max_length=200)
    prenom_util = models.CharField(max_length=200)
    mail_util = models.EmailField()
    password_util = models.CharField(max_length=50)
    login_util = models.CharField(max_length=30)
    grade_util = models.CharField(max_length=50)
    spec_formation = models.CharField(max_length=80)
    type_formation = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de creation")

    def __str__(self):
        return self.id


# Classe ORM Categorie
class Categorie(models.Model):
    lib_categ = models.CharField(max_length=200)
    administrateur = models.ForeignKey('Administrateur')

    def __str__(self):
        return self.id


# Classe ORM Formation
class Formation(models.Model):
    lib_form = models.CharField(max_length=80)
    date_deb_form = models.DateField(auto_now=False, auto_now_add=False)
    date_fin_form = models.DateField(auto_now=False, auto_now_add=False)
    categorie = models.ForeignKey('Categorie')

    def __str__(self):
        return self.id


# Classe ORM Apprenant
class Apprenant(models.Model):
    nom_util = models.CharField(max_length=200)
    prenom_util = models.CharField(max_length=200)
    mail_util = models.EmailField()
    password_util = models.CharField(max_length=50)
    login_util = models.CharField(max_length=30)
    grade_util = models.CharField(max_length=50)
    diplome_appr = models.CharField(max_length=80)
    formation = models.ForeignKey('Formation')

    def __str__(self):
        return self.id


# Classe ORM Regroupement
class Regroupement(models.Model):
    date_group = models.DateField(auto_now=False, auto_now_add=False)
    formation = models.ForeignKey('Formation')

    def __str__(self):
        return self.id


# Classe ORM Cours
class Cours(models.Model):
    lib_cour = models.CharField(max_length=80)
    formation = models.ForeignKey('Formation')

    def __str__(self):
        return self.id


# Classe ORM Chapitre
class Chapitre(models.Model):
    lib_chap = models.CharField(max_length=80)
    cours = models.ForeignKey('Cours')

    def __str__(self):
        return self.id


# Classe ORM Ressource
class Ressource(models.Model):
    lib_ress = models.CharField(max_length=80)
    type_ress = models.CharField(max_length=50)
    chapitre = models.ForeignKey('Chapitre')

    def __str__(self):
        return self.id


# Classe ORM Animer
class Animer(models.Model):
    id_util = models.ForeignKey('Formateur')
    id_form = models.ForeignKey('Formation')

    def __str__(self):
        return self.id


# Classe ORM Test
class Test(models.Model):
    id_util = models.ForeignKey('Apprenant')
    id_form = models.ForeignKey('Formation')

    date_test = models.DateField(auto_now=False, auto_now_add=False)
    note_test = models.IntegerField()

    def __str__(self):
        return self.id
