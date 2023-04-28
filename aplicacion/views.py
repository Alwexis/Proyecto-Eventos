from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, authenticate, get_user_model, logout as django_logout
from aplicacion.models import Evento, Ticket, Venta, Venta
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

@login_required(login_url='login')
def evento(request, id):
    evento = Evento.objects.get(id=id)
    if request.method == 'POST':
        vip, cancha, galeriaLateral, galeriaCentral = int(request.POST['vip']), int(request.POST['cancha']), int(request.POST['galeriaLateral']), int(request.POST['galeriaCentral'])
        if vip == 0 and cancha == 0 and galeriaLateral == 0 and galeriaCentral == 0:
            return render(request, 'aplicacion/evento.html', { 'evento': evento, 'error': 'Debe seleccionar al menos una ubicación' })
        else:
            changes = False
            if vip > 0:
                evento.asientos -= int(vip)
                evento.asientos_vip -= int(vip)
                changes = True

                ticketVip = Ticket(evento=evento, cantidad=int(vip), tipoAsiento='vip', comprador=request.user)
                ticketVip.save()

                monto = (evento.precio * 2) * int(vip)
                venta = Venta(ticket=ticketVip, monto=monto, cantidad_articulos=vip)
                venta.save()
            if cancha > 0:
                evento.asientos -= int(cancha)
                evento.asientos_cancha -= int(cancha)
                changes = True

                ticketCancha = Ticket(evento=evento, cantidad=int(cancha), tipoAsiento='cancha', comprador=request.user)
                ticketCancha.save()
                
                monto = (evento.precio +  evento.precio * 0.5) * int(vip)
                venta = Venta(ticket=ticketCancha, monto=monto, cantidad_articulos=cancha)
                venta.save()
            if galeriaLateral > 0:
                evento.asientos -= int(galeriaLateral)
                evento.asientos_galeriaLateral -= int(galeriaLateral)
                changes = True

                ticketGaleriaLateral = Ticket(evento=evento, cantidad=int(galeriaLateral), tipoAsiento='galeria_lateral', comprador=request.user)
                ticketGaleriaLateral.save()
                
                monto = evento.precio * int(vip)
                venta = Venta(ticket=ticketCancha, monto=monto, cantidad_articulos=galeriaLateral)
                venta.save()
            if galeriaCentral > 0:
                evento.asientos -= int(galeriaCentral)
                evento.asientos_galeriaCentral -= int(galeriaCentral)
                changes = True

                ticketGaleriaCentral = Ticket(evento=evento, cantidad=int(galeriaCentral), tipoAsiento='galeria_central', comprador=request.user)
                ticketGaleriaCentral.save()
                
                monto = (evento.precio +  evento.precio * 0.25) * int(vip)
                venta = Venta(ticket=ticketCancha, monto=monto, cantidad_articulos=galeriaCentral)
                venta.save()
            if changes:
                evento.save()
                return redirect('/mis-eventos', { 'action': 'tickets_bought' })
    return render(request, 'aplicacion/evento.html', { 'evento': evento })

@login_required(login_url='login')
def misEventos(request):
    eventos = []
    tickets = Ticket.objects.filter(comprador=request.user).values()
    for ticket in tickets:
        evento = Evento.objects.get(id=ticket['evento_id'])
        ticket['tipoAsientoFixed'] = ticket['tipoAsiento'].replace('_', ' ').capitalize()
        monto = 0
        if ticket['tipoAsiento'] == 'vip':
            monto = (evento.precio * 2) * ticket['cantidad']
        elif ticket['tipoAsiento'] == 'cancha':
            monto = (evento.precio +  evento.precio * 0.5) * ticket['cantidad']
        elif ticket['tipoAsiento'] == 'galeria_lateral':
            monto = evento.precio * ticket['cantidad']
        elif ticket['tipoAsiento'] == 'galeria_central':
            monto = (evento.precio +  evento.precio * 0.25) * ticket['cantidad']

        eventos.append({ 'evento': evento, 'venta': round(monto), 'ticket': ticket })
    # Obtener el agente del usuario
    user_agent = request.META.get('HTTP_USER_AGENT')
    user_agent_parsed = parse(user_agent)
    # Verificar si el agente del usuario es un dispositivo móvil
    is_mobile = user_agent_parsed.is_mobile

    return render(request, 'aplicacion/mis-eventos.html', { 'eventos': eventos, 'is_mobile': is_mobile })

@login_required(login_url='login')
def perfil(request):
    user = request.user
    
    return render(request, 'aplicacion/perfil.html', { 'usuario': user })

def acercade(request):
    return render(request, 'aplicacion/acerca-de.html')