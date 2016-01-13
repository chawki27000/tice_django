from django.contrib import admin
from gestion.models import Administrateur, Formateur, Categorie, Formation, Apprenant
from gestion.models import Regroupement, Cours, Chapitre, Ressource, Animer, Test


# Class d'administration
class AdministrateurAdmin(admin.ModelAdmin):
    list_display = ('nom_util', 'prenom_util', 'date')
    list_filter = ('nom_util', 'login_util',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('nom_util', 'email_util')


# Register your models here.
admin.site.register(Administrateur, AdministrateurAdmin)
admin.site.register(Formateur)
admin.site.register(Categorie)
admin.site.register(Formation)
admin.site.register(Apprenant)
admin.site.register(Regroupement)
admin.site.register(Cours)
admin.site.register(Chapitre)
admin.site.register(Ressource)
admin.site.register(Animer)
admin.site.register(Test)
