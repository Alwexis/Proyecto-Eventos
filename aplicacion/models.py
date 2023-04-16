from django.db import models

# Create your models here.
class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=1024)
    fecha = models.TextField(max_length=128)
    fechaMilisegundos = models.IntegerField()
    lugar = models.TextField(max_length=1024)
    precio = models.IntegerField()
    asientos = models.IntegerField()
    asientos_vip = models.IntegerField()
    asientos_cancha = models.IntegerField()
    asientos_galeriaLateral = models.IntegerField()
    asientos_galeriaCentral = models.IntegerField()
    url = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    rut = models.IntegerField(primary_key=True, unique=True)
    dv = models.TextField(max_length=1)
    nombres = models.TextField()
    apellidos = models.TextField()
    correo_electronico = models.EmailField(unique=True)
    numero_telefonico = models.IntegerField(unique=True)
    contrasena = models.TextField()
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombres

class Ticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    comprador = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.id}"

class Venta(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
    monto = models.IntegerField()
    cantidad_articulos = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}"