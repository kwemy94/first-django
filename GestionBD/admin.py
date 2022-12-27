from django.contrib import admin
from GestionBD.models import Employe, Entreprise

# Register your models here.
admin.site.register(Entreprise)

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    #element à display avec l'attribut de classe list_display
    list_display = ('name', 'fonction', 'salaire', 'email')
    #créer un filtre sur les données avec l'attribut de classe list_filter
    list_filter = ('name', 'fonction', 'email')
    search_fields = ('name',)
