#from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('Servicios', views.Servicios, name='Servicios'),
    path('Nosotros', views.Nosotros, name='Nosotros'),
    path('Entrenadores', views.Entrenadores, name='Entrenadores'),
    path('Contactanos', views.Contactanos, name='Contactanos'),
    
    
]                           