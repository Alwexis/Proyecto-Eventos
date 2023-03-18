from proyecto.urls import path
from aplicacion.views import home

# Patterns
urlpatterns = [
    path('', home, name="home")
]