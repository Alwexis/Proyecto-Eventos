from proyecto.urls import path
from aplicacion.views import home, login, logout, registro, evento, misEventos, perfil, acercade

# Patterns
urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('registro', registro, name="registro"),
    path('evento/<int:id>/', evento, name='evento'),
    path('mis-eventos', misEventos, name='mis-eventos'),
    path('perfil', perfil, name='perfil'),
    path('acerca-de', acercade, name='acerca-de')
]