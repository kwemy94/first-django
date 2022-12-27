from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from GestionBD.models import Employe, Entreprise
from AppTwo.forms import LoginForms

from rest_framework.views import APIView
from AppTwo.serializers import EntrepriseSerializer, EmployeSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def index(request):
    donnees ={'ras': 'juste des test de similtude django / laravel'}
    loginForm = LoginForms()


    if len(request.POST) > 0:
        form = LoginForms(request.POST)
        # if 'login' not in request.POST or  'pwd' not in request.POST :
        #     error = 'Login et mot de passe requis'
        if form.is_valid():
            return render(request, 'index.html', {'loginForm': form})
        else:
            # if request.POST['login'] == '' or  request.POST['pwd'] == '' :
            #     error = 'Tous les champs sont obligatoires !'
            #     return render(request, 'index.html', {'error': error})

            username = request.POST['login']
            pwd = request.POST['pwd']

            if username != 'gtiwa@utecq.dev' or pwd != 'password':
                error = "Login ou mot de passe incorrect"
                return render(request, 'index.html', {'loginForm': form})
            else:
                return redirect('/admin')
    else:
        return render(request, 'index.html', {'loginForm': loginForm, 'django': 'first app with django, test filter'})


    # return render(request, 'index.html', {'cdate': datetime.now})

def store(request):
    return HttpResponse("<em> Route with url </em>")

def help(request):
    msg = {'title': "Page d'aide", 'content': 'Bienvenue sur le site  2S test Djangui'}
    entreprises = Entreprise.objects.order_by('name')
    employes = Employe.objects.order_by('name')
    
    return render(request, 'help.html', {'msg': msg, 'entreprises': entreprises, 'employes': employes})



# class EntrepriseView(APIView):

#     # Redéfinition de la méthode get
#     def get(self, *args, **kwargs):
#         entreprises = Entreprise.objects.all()
#         serializer = EntrepriseSerializer(entreprises, many=True)
#         return Response(serializer.data)

class EntrepriseViewset(ModelViewSet):
    # Définition du sérializer à utiliser dans l'attribut de class ci dessous
    serializer_class = EntrepriseSerializer
    permission_classes = (IsAuthenticated,)

    # Récrire la méthode get_queryset
    def get_queryset(self):
        # return Entreprise.objects.all()
        # queryset = Entreprise.objects.all()
        # entreprise_id = self.request.get('id')

        # if entreprise_id :
        #     queryset = queryset.filter(entreprise_id=entreprise_id)
        return Entreprise.objects.filter(status = True)

class EmployeView(APIView):

    def get(self, *args, **kwargs):
        employe = Employe.objects.all()
        serializer = EmployeSerializer(employe, many = True)
        return Response(serializer.data)
