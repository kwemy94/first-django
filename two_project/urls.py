"""two_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppTwo import views
from django.conf.urls import include
from django.urls import re_path as url
from AppTwo.views import EntrepriseViewset, EmployeView
from rest_framework import routers


# Définition du router
router = routers.SimpleRouter()

# Déclaration d'1 url basé sur le mot clé 'entreprise'
router.register('entreprise', EntrepriseViewset, basename='entreprise')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    path('app-two', views.index, name='index'),
    # path('with-url', include('AppTwo.urls')),
    url(r'^test-app/', include('AppTwo.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # Ajout des urls du router
    path('api/', include(router.urls)),
    # path('api/entreprise/', EntrepriseView.as_view()),
    path('api/employe/', EmployeView.as_view()),

    #auth route
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
    
]
