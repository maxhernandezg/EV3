from django.shortcuts import render
from .models import Alumno,Genero
# Create your views here.

# Función para mostrar el índice principal con todos los alumnos
def index(request):
    # Recupera todos los objetos Alumno de la base de datos
    alumnos = Alumno.objects.all()  # SELECT * FROM alumno
    # Contexto para pasar a la plantilla
    context = {"alumnos": alumnos}
    # Renderiza la plantilla 'index.html' con el contexto de alumnos
    return render(request, 'alumnos/index.html', context)

# Función para gestionar el CRUD de alumnos
def crud(request):
    # Recupera todos los objetos Alumno de la base de datos
    alumnos = Alumno.objects.all()  # SELECT * FROM alumno
    # Contexto para pasar a la plantilla
    context = {"alumnos": alumnos}
    # Renderiza la plantilla 'alumnos_list.html' con el contexto de alumnos
    return render(request, 'alumnos/alumnos_list.html', context)

# Función para agregar un nuevo alumno
def alumnosAdd(request):
    # Si el método de la solicitud no es POST, muestra el formulario
    if request.method != "POST":
        # Recupera todos los objetos Genero de la base de datos
        generos = Genero.objects.all()  # SELECT * FROM genero
        # Contexto para pasar a la plantilla
        context = {'generos': generos}
        # Renderiza la plantilla 'alumnos_add.html' con el contexto de géneros
        return render(request, 'alumnos/alumnos_add.html', context)
    else:
        # Si el método es POST, procesa los datos del formulario
        # Recupera los datos del formulario y los asigna a variables locales
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        # Busca el objeto Genero correspondiente al género ingresado
        objGenero = Genero.objects.get(id_genero=genero)

        # Crea un objeto Alumno con los datos del formulario
        obj = Alumno.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=activo
        )

        # Guarda el objeto Alumno en la base de datos
        obj.save()
        # Mensaje de confirmación
        context = {'mensaje': "Ok, datos guardados..."}
        # Renderiza la plantilla 'alumnos_add.html' con el mensaje de confirmación
        return render(request, 'alumnos/alumnos_add.html', context)

# Función para eliminar un alumno
def alumnos_del(request, pk):
    # Contexto inicial vacío
    context = {}
    try:
        # Intenta recuperar el objeto Alumno por su clave primaria (rut)
        alumno = Alumno.objects.get(rut=pk)
        # Elimina el objeto Alumno
        alumno.delete()
        # Mensaje de éxito
        mensaje = "Bien, datos eliminados..."
        # Recupera todos los objetos Alumno de la base de datos
        alumnos = Alumno.objects.all()
        # Contexto actualizado con la lista de alumnos y el mensaje
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        # Renderiza la plantilla 'alumnos_list.html' con el contexto
        return render(request, 'alumnos/alumnos_list.html', context)
    except:
        # Si ocurre un error (por ejemplo, el alumno no existe), maneja la excepción
        mensaje = "Error, el alumno no existe..."
        # Recupera todos los objetos Alumno de la base de datos
        alumnos = Alumno.objects.all()
        # Contexto actualizado con la lista de alumnos y el mensaje de error
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        # Renderiza la plantilla 'alumnos_list.html' con el contexto
        return render(request, 'alumnos/alumnos_list.html', context)
    
def alumnos_findEdit(request, pk):

    if pk != "":
        alumno = Alumno.objects.get(rut=pk)
        generos = Genero.objects.all()

        print(type(alumno.id_genero.genero))

        context = {'alumno': alumno, 'generos': generos}

        if alumno:
            return render(request, 'alumnos/alumnos_edit.html', context)
        else:
            context = {'mensaje': "Error, el rut no existe..."}
            return render(request, 'alumnos/alumnos_list.html', context)       

def alumnosUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero_id = request.POST["genero"]  # Este es el ID del genero, no la instancia

        # Obtén la instancia de Genero utilizando el ID
        objGenero = Genero.objects.get(id_genero=genero_id)

        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = 1

        # Crea una instancia de Alumno y asigna los valores
        alumno = Alumno()
        alumno.rut = rut
        alumno.nombre = nombre
        alumno.apellido_paterno = aPaterno
        alumno.apellido_materno = aMaterno
        alumno.fecha_nacimiento = fechaNac
        alumno.id_genero = objGenero  # Asigna la instancia de Genero, no el ID
        alumno.telefono = telefono
        alumno.email = email
        alumno.direccion = direccion
        alumno.activo = activo
        alumno.save()

        generos = Genero.objects.all()
        context = {'mensaje': "Ok, datos actualizados...",
                   'generos': generos,
                   'alumno': alumno}
        return render(request, 'alumnos/alumnos_edit.html', context)
    else:
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos}
        return render(request, 'alumnos/alumnos_list.html', context)