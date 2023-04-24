from proyecto.urls import path
from aplicacion.views import home, login, logout, registro, evento

# Patterns
urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('registro', registro, name="registro"),
    path('evento/<int:id>/', evento, name='evento'),
]