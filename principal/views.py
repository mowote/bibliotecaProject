from django.shortcuts import render
from django.db.models import Q
from .models import Libro, Evento, Usuario, Reserva
from django.contrib.auth.models import  User
from django.utils import timezone



# Create your views here.

def principal(request):
    libros = Libro.objects.all()
    economia = Libro.objects.filter(genero= "economia")[:5]
    infantil = Libro.objects.filter(genero= "infantil")[:5]
    literatura_general = Libro.objects.filter(genero= "literatura_general")[:5]
    agropecuaria = Libro.objects.filter(genero= "agropecuaria")[:5]
    if request.user.is_authenticated:
        email= request.user.email
        usuario = Usuario.objects.filter (correo=email)
        return render(request, 'principal.html', {"libros": libros, "economia":economia, "infantil": infantil,"literatura_general": literatura_general,"agropecuaria": agropecuaria,"usuario":usuario})
    else:
        return render(request, 'principal.html', {"libros": libros, "economia":economia, "infantil": infantil,"literatura_general": literatura_general,"agropecuaria": agropecuaria})

def evento(request):
    evento = Evento.objects.all() 
    return render(request,'evento.html',{"evento":evento})

def usuario(request,username=None):
    email= request.user.email
    usuario = Usuario.objects.filter (correo=email)[:1]
    hoy = timezone.now
    reservas = Reserva.objects.filter(identificacion=usuario)
    return render(request,'usuario.html',{"usuario":usuario, "reservas":reservas, "hoy": hoy})


    libros = Libro.objects.all()
    return render(request,'libros.html', {"libros": libros})
def libros(request):
    libros = Libro.objects.all()
    if request.user.is_authenticated:
        email= request.user.email
        usuario = Usuario.objects.filter (correo=email)
        return render(request, 'libros.html', {"libros": libros,"usuario":usuario})
    else:
        return render(request, 'libros.html', {"libros": libros, })
    


def reservas(request):
    return render(request,'reservas.html', {"reservas"})



def busquedas(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        resultados = Libro.objects.filter(Q(nombre__icontains= busqueda) |
                                           Q(genero__icontains=busqueda) |
                                           Q(autor__icontains=busqueda)).distinct()
        

        return render(request, 'busquedas.html', {"busqueda": busqueda, "resultados":resultados} )
    else:
        return render(request, 'busquedas.html', )