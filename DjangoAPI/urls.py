"""DjangoAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from webserver.views import Dados, DadosViewSet
from rest_framework import routers

# Aqui definimos a rota principal da nossa API
router = routers.DefaultRouter()
# Então registramos as subrotas para nossos modelos, dando como argumento o viewset desse modelo
router.register('dados', DadosViewSet, basename='Dados')

# Em seguida registramos nossa rota principal (string vazia) no include urls ligado a router (objeto de DefaultRouter)
urlpatterns = [
    # trocamos o path admin aqui para dar um reforço na segurança da nossa API
    path('painel/', admin.site.urls),
    # Algum erro ocorreu com o honey pot, deixe isso aqui e tente consertar depois
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', include(router.urls)),
]
