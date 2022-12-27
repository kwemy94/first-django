from rest_framework.serializers import ModelSerializer
from GestionBD.models import Entreprise, Employe

class EntrepriseSerializer(ModelSerializer):
    class Meta:
        model = Entreprise #définir le model à utiliser
        fields = ['id', 'name', 'localisation']   #champ à recupérer dans la bd


class EmployeSerializer(ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'