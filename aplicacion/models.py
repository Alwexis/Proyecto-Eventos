from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=1024)
    fecha = models.TextField(max_length=128)
    fechaMilisegundos = models.IntegerField()
    lugar = models.TextField(max_length=1024)
    imagen = models.TextField()
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
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Validar dirección de correo electrónico
        if not email:
            raise ValueError('El Email debe ser establecido')
        email = self.normalize_email(email)
        # Crear instancia del modelo de usuario
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Crear usuario con privilegios de superusuario
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    #* Estos son los atributos que Django tiene y requiere por defecto.
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    #* Estos son los atributos que yo quiero añadir al nuevo modelo de Usuario
    rut = models.IntegerField(primary_key=True, unique=True)
    dv = models.TextField(max_length=1)
    nombres = models.TextField()
    apellidos = models.TextField()
    numero_telefonico = models.IntegerField(null=True)
    #* Definir el gestor de usuarios personalizado
    objects = CustomUserManager()
    #* Esto es lo que se va a requerir para iniciar sesión.
    #* Es un campo del modelo del Usuario.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombres']

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Ticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipoAsiento = models.TextField(max_length=128)
    cantidad = models.IntegerField()
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