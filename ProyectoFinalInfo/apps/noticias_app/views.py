from time import timezone
from django.shortcuts import render
# from django.http import HttpResponse
from .models import Noticia,Comentarios,Categoria
from django.http.response import Http404

# Create your views here.

def base(request):
    return render(request, 'base.html', {})

def index(request):
    return render(request, 'index.html', {})

def noticias(request):
    lista_de_noticias = Noticia.objects.all().order_by('creado')
    context = {
        "noticias" : lista_de_noticias,
    }
    return render(request, 'noticias.html', context)

def eventos(request):
    return render(request, 'eventos.html', {})

def nosotros(request):
    return render(request, 'nosotros.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def noticiadetalle(request,id):
    try:
        data = Noticia.objects.get(id=id)
    except Noticia.DoesNotExist:
        raise Http404('La noticia solicitada no existe.')

    context = {
        "noticia" : data,
    }

    return render(request, 'noticias-detalle.html', context)