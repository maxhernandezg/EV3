"""instituto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# instituto/urls.py

# Importa las funciones necesarias para definir las URL del proyecto
from django.contrib import admin
from django.urls import path, include

# Lista de patrones de URL para el proyecto
urlpatterns = [
    # URL para el sitio de administración de Django
    path('admin/', admin.site.urls),

    # Incluir las URLs definidas en la aplicación 'alumnos'
    # Esto redirige cualquier URL que comience con 'alumnos/' a las URLs definidas en 'alumnos/urls.py'
    path('alumnos/', include('alumnos.urls')),
]