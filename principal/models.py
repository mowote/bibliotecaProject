from django.db import models

# Create your models here.
class Libro(models.Model):
    
    GENERO_LIBRO= [
        ("infantil","Infantil"),
        ("literatura_general", "literatura general"),
        ("deporte","Deporte"),
        ("economia","Economia"),
        ("matematicas","Matematicas"),
        ("secretos_para_contar","Secretos para Contar"),
        ("sexualidad","Sexualidad"),
        ("tecnologia","Tecnologia"),
        ("religion","Religion"),
         
        
    ]
    
    signatura=models.CharField("Signatura", max_length=50)
    nombre= models.CharField("Nombre", max_length=50)
    genero= models.CharField("Genero", max_length=50, choices=GENERO_LIBRO)
    autor= models.CharField("Autor", max_length=120)
    resena= models.CharField("Reseña", max_length=1500)
    estado= models.CharField("Estado", max_length=50) 
    unidades= models.IntegerField("Unidades")
    imagen= models.ImageField("Imagen", upload_to="static/db")  
    
    def __str__(self):
        return self.nombre 
    
class Usuario(models.Model):
    TIPO_DOCUMENTO=[
        ("ti","Tarjeta identidad"),
        ("cc","Cedula"),
        ("ce","Cedula estrangeria")
    ]
    
    nombre= models.CharField("Nombre", max_length=50)
    apellido= models.CharField("Apellido", max_length=50)
    tipo_documeto= models.CharField("Tipo documento", max_length=50, choices=TIPO_DOCUMENTO)
    identificacion= models.IntegerField(" Numero Identificación")
    edad= models.IntegerField("Edad")
    telefono= models.IntegerField("Telefono")
    correo= models.EmailField("Correo electronico", max_length=254)
    direccion= models.CharField("Direccion de residencia", max_length=50)
    departamento= models.CharField("Departamento", max_length=50)
    municipio= models.CharField("Municipio", max_length=50)
    user= models.CharField("usuario",max_length=70)
    pasword= models.CharField("Contraseña",max_length=70)
    
    def __str__(self):
        return self.nombre
    
class Evento(models.Model):
    identificacion_evento= models.IntegerField("Identificación del evento")
    nombre_evento=models.CharField("Nombre del evento", max_length=300)
    hora_inicio=models.DateTimeField("Hora inicio", auto_now_add=False)
    hora_fin=models.DateTimeField("Hora de finalización", auto_now_add=False)
    lugar=models.CharField("lugar", max_length=300)
    nombre_tallerista=models.CharField("Nombre del tallerista", max_length=300)
    cargo=models.CharField("Cargo", max_length=300)
    imagen= models.ImageField("Imagen", upload_to="static/db") 
    
    def __str__(self):
        return self.nombre_evento 
        
    
class Reserva(models.Model):
    fecha_inicial=models.DateField("Fecha prestamo", auto_now_add=True)
    fecha_devolucion=models.DateField("Fecha devolución" )
    identificacion= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    signatura=models.ForeignKey(Libro, on_delete=models.CASCADE)
    
    def __str__(self):
     return 'Reserva del libro {self.libro} por {self.usuario}'    
        
    