# alumnos/urls.py


# Importa la función path para definir las rutas URL y las vistas desde el módulo views
from django.urls import path
from . import views

# Lista de patrones de URL para la aplicación 'alumnos'
urlpatterns = [
    # Ruta URL para la vista 'index'
    path('index/', views.index, name='index'),

    # Ruta URL para la vista 'crud'
    path('crud/', views.crud, name='crud'),

    # Ruta URL para la vista 'alumnosAdd', utilizada para añadir nuevos alumnos
    path('alumnosAdd/', views.alumnosAdd, name='alumnosAdd'),

    # Ruta URL para la vista 'alumnos_del', que elimina un alumno basado en su 'rut'
    # <str:pk> es un parámetro de la URL que se pasa a la vista
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),

    # Ruta URL para la vista 'alumnos_findEdit', que busca y edita un alumno basado en su 'rut'
    # <str:pk> es un parámetro de la URL que se pasa a la vista
    path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),

    # Ruta URL para la vista 'alumnosUpdate', utilizada para actualizar los datos de un alumno
    path('alumnosUpdate/', views.alumnosUpdate, name='alumnosUpdate'),

    # Ruta URL para la vista 'crud_generos', que gestiona el CRUD de géneros
    path('crud_generos', views.crud_generos, name='crud_generos'),

    # Ruta URL para la vista 'generosAdd', utilizada para añadir nuevos géneros
    path('generosAdd', views.generosAdd, name='generosAdd'),

    # Ruta URL para la vista 'generos_del', que elimina un género basado en su 'id_genero'
    # <str:pk> es un parámetro de la URL que se pasa a la vista
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),

    # Ruta URL para la vista 'generos_edit', que edita un género basado en su 'id_genero'
    # <str:pk> es un parámetro de la URL que se pasa a la vista
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),
]