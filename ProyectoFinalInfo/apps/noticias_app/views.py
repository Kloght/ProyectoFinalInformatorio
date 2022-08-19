from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def base(request):
    return render(request, 'base.html', {})

def index(request):
    return render(request, 'index.html', {})

def noticias(request):
    return render(request, 'noticias.html', {})

def eventos(request):
    return render(request, 'eventos.html', {})

def nosotros(request):
    return render(request, 'nosotros.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})