from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import re
from aplicacion.models import Usuario

# Create your views here.
@login_required(login_url="login")
def home(request):
    return render(request, 'aplicacion/home.html')

def login(request):
    if request.method == 'POST':
        email_rut = request.POST['email-rut']
        pwd = request.POST['password']
        email_regex = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        usuario = None
        if re.match("[0-9]{7,8}-([0-9]|k){1}", email_rut):
            print('Es rut')
            nuevoRut = email_rut.split('-')[0]
            usuario = Usuario.objects.get(rut=nuevoRut)
            if usuario:
                print(usuario)
        elif re.match(email_regex, email_rut):
            print('Es correo')
            usuario = Usuario.objects.get(correo_electronico=nuevoRut)
            if usuario:
                print(usuario)
        else:
            print('Inválido')
    return render(request, 'aplicacion/login.html')

def registro(request):
    if request.method == 'POST':
        print('Post')
    return render(request, 'aplicacion/registro.html')