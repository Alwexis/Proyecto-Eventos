from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, authenticate, get_user_model, logout as django_logout
from aplicacion.models import Evento
from django.core.paginator import Paginator
from django.http import Http404
from user_agents import parse

# Create your views here.
def home(request):
    eventos = Evento.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    # Obtener el agente del usuario
    user_agent = request.META.get('HTTP_USER_AGENT')
    user_agent_parsed = parse(user_agent)
    # Verificar si el agente del usuario es un dispositivo móvil
    is_mobile = user_agent_parsed.is_mobile

    try:
        if is_mobile:
            paginator = Paginator(eventos, 14)
        else:
            paginator = Paginator(eventos, 28)
        eventos = paginator.page(page)
    except:
        raise Http404('No se encontraron eventos')

    return render(request, 'aplicacion/home.html', { 'eventos': eventos, 'is_mobile': is_mobile })

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['password']
        authUser = authenticate(request, email=email, password=pwd)
        if authUser is not None:
            django_login(request, authUser)
            return redirect('/', { 'action': 'user_logged' })
        else:
            return render(request, 'aplicacion/login.html', {'error': 'cannot_log_in'})
    return render(request, 'aplicacion/login.html')

def logout(request):
    django_logout(request)
    return redirect('login')

def registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        rut = request.POST['rut'].split('-')[0]
        dv = request.POST['rut'].split('-')[1]
        correo = request.POST['email']
        contrasena = request.POST['password']

        UserModel = get_user_model()
        usuario = UserModel.objects.create_user(rut=rut, password=contrasena, dv=dv, nombres=nombre, apellidos=apellido, email=correo)
        try:
            usuario.save()
            authenticate(request, rut=rut, password=contrasena)
            login(request)
            return redirect('/', { 'action': 'user_registered' })
        except Exception as e:
            return render(request, 'aplicacion/registro.html', {'error': 'Error al registrar usuario'})
    return render(request, 'aplicacion/registro.html')

def evento(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, 'aplicacion/evento.html', { 'evento': evento })