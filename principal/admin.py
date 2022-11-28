from django.contrib import admin
from .models import Libro,Evento,Usuario,Reserva

class libroAdmin(admin.ModelAdmin):
      list_display=("nombre","signatura","genero","autor","estado","unidades")     
admin.site.register(Libro, libroAdmin)

class usuarioAdmin(admin.ModelAdmin):
     list_display=("nombre","apellido","tipo_documeto","identificacion","edad","telefono","correo","direccion","departamento",
                   "municipio","user","pasword")    
admin.site.register(Usuario,usuarioAdmin)

class eventoAdmin(admin.ModelAdmin):
     list_display=("nombre_evento","hora_inicio","hora_fin","lugar","nombre_tallerista","cargo")
     list_filter=("hora_inicio",)
admin.site.register(Evento,eventoAdmin)    
    
class reservaAdmin(admin.ModelAdmin):
     list_display=("signatura","fecha_inicial","fecha_devolucion", "identificacion")
     list_filter=("fecha_devolucion","fecha_inicial")
admin.site.register(Reserva, reservaAdmin)    
    

   