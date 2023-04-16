from proyecto.urls import path
from aplicacion.views import home, login

# Patterns
urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login")
]