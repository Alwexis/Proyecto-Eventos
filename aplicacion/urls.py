from proyecto.urls import path
from aplicacion.views import home, login, registro

# Patterns
urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('registro', registro, name="registro"),
]