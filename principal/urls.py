from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.principal, name='principal'),
    path('evento/',views.evento, name="evento"),
    path('usuario/<str:username>',views.usuario, name="usuario"),
    path('libros/',views.libros, name="libros"),
   
    path('busqueda/',views.busquedas, name="busqueda"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)