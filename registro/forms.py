from django import forms 
from principal.models import Usuario
from principal.models import Libro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
  
    email= forms.EmailField(label="Correo electronico",)
    password1= forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label='Confirmar contraseña', widget= forms.PasswordInput)
    
    class Meta:
        model= User
        fields=['username','email','password1', 'password2']
        help_texts= {k:"" for k in fields}
        
class datos_PersonalesForm(forms.ModelForm):
    
    class Meta:
        model= Usuario
        fields = ['nombre','apellido','tipo_documeto','identificacion','edad','telefono','correo','direccion','departamento','municipio']
   
class reservasForm(forms.ModelForm):
    
    class Meta:
        model= Libro
        fields = "__all__"
        
        
        
    
        