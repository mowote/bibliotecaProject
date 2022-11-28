from django.shortcuts import render, redirect
from .forms import UserRegisterForm, datos_PersonalesForm,reservasForm;
from django.contrib import messages
from principal.models import Libro, Reserva, Usuario
import datetime

# Create your views here.

def registro(request):
    form= UserRegisterForm()
    if request.method == 'POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal')
            messages.success(request,"se ha registrado exitosamente")
    else:
        form= UserRegisterForm()   
    
    return render (request, 'registro.html',{'form':form})


def infoPersonal(request):
    form= datos_PersonalesForm()
    if request.method == 'POST':
        form= datos_PersonalesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"se ha registrado exitosamente")
    else:
        form= datos_PersonalesForm()   
    
    return render (request, 'infoPersonal.html',{'form':form})

def reservas(request, libro=None):
    
    libros = Libro.objects.get(id = libro)
    actualizar = Libro.objects.get(id = libro)
    email = request.user.email
    usuario = Usuario.objects.get(correo=email)
    actualizar.unidades -= 1
    if actualizar.unidades == 0:
        actualizar.estado = "En prestamo"
    actualizar.save()
    
    # Sumar días a la entrega
    hoy = datetime.datetime.utcnow()
    entrega = hoy + datetime.timedelta(days=15)
    reservar = Reserva(fecha_devolucion = entrega, identificacion = usuario, signatura = libros )
    reservar.save()
    messages.success(request, f'Su reserva para {libros.nombre} ha sido exitosa')
    return render (request, 'reservas.html', {"libros":libros})

def noDisponible(request):
    
    
    return render (request, 'noDisponible.html')
