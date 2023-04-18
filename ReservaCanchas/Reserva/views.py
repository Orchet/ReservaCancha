from django.shortcuts import render
from django.http import HttpResponse
from .models import Cancha
from .models import Persona
from .models import Horario
from django.views.generic import TemplateView

# Create your views here.

#Definicion Anterior
#def getInfoCanchaById (request, id_cancha):
#    #Obtener cancha por su id utilizando ORM
#    cancha = Cancha.objects.get(id=id_cancha)
#    result = f"Cancha: {cancha.nombre}, Descripción: {cancha.descripcion}"
#    return HttpResponse(result)

#Definicion Nueva
def getInfoCanchaById (request, id_cancha):
    #Obtener cancha por su id utilizando ORM
    cancha = Cancha.objects.get(id=id_cancha)
    horarios = Horario.objects.filter(cancha__id=cancha.id)
    #return render (request, "cancha.html", {'nombre': cancha.nombre, 'descripcion': cancha.descripcion})
    return render (request, "info_cancha.html", {'nombre_cancha': cancha.nombre, 'desc_cancha': 
    cancha.descripcion, 'horarios':horarios})


def getPersonaById (request, id_persona):
    #Obtener persona por su id utilizando ORM
    persona = Persona.objects.get(id=id_persona)
    result = f"Nombre: {persona.nombre}, Apellido: {persona.apellido}, Correo: {persona.correo}"
    return HttpResponse(result)

class MainView(TemplateView):
    template_name = "main.html" 

def getListadoCanchas(request):
    canchas = Cancha.objects.all()
    nombre_canchas = []
    for cancha in canchas:
        nombre_canchas.append((cancha.id, cancha.nombre))
    
    return render(request, "canchas.html", {'listado': nombre_canchas})
