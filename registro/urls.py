from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('registro/', views.registro, name="registro"),
    path("login/", LoginView.as_view(template_name="iniciar_sesion.html"),name="login"),
    path("logout/", LogoutView.as_view(template_name="iniciar_sesion.html"),name="logout"),
    path('infoPersonal/', views.infoPersonal, name="infoPersonal"),
    path('reservas/<int:libro>/', views.reservas, name="reservas"),
    path('noDisponible/', views.noDisponible, name="noDisponible"),
]