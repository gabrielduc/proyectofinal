from django.shortcuts import render

# Create your views here.


def index(request):
    context={}
    return render (request, 'gymapp/index.html', context)

def Servicios(request):
    context={}
    return render (request, 'gymapp/Servicios.html', context)

def Nosotros(request):
    context={}
    return render (request, 'gymapp/Nosotros.html', context)

def Entrenadores(request):
    context={}
    return render (request, 'gymapp/Entrenadores.html', context)

def Contactanos(request):
    context={}
    return render (request, 'gymapp/Contactanos.html', context)
