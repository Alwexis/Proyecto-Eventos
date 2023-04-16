from django.contrib import admin
from aplicacion.models import Usuario, Ticket, Evento, Venta

# Register your models here.
class admUsuario(admin.ModelAdmin):
    class Meta:
        model = Usuario

class admTicket(admin.ModelAdmin):
    class Meta:
        model = Ticket
    
class admEvento(admin.ModelAdmin):
    class Meta:
        model = Evento
    
class admVenta(admin.ModelAdmin):
    class Meta:
        model = Venta

register = [Usuario, Evento, Ticket, Venta]
classes = [admUsuario, admEvento, admTicket, admVenta]
for x in range(0, len(register), 1):
    admin.site.register(register[x], classes[x])