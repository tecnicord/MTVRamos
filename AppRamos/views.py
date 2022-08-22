from django.shortcuts import render
from AppRamos.models import Datos
from django.http import HttpResponse
from datetime import datetime
def familia(request):
    return HttpResponse("Esta es la familia Ramos: Miguel, Teresita, Mateo y Tomas")

def papa(request, nombre):
    padre = f"El padre de esta familia se llama {nombre}"

    return HttpResponse(padre)

def template_1(request):
    context = {
        'Padre': "Miguel",
        'Madre': "Teresita",
        'lista': [34, 38, 62, 64],
        'ahora': datetime.now()
    }

    return render(request, 'template1.html', context)


def datos(request):
    datos1 = Datos(nombre="Miguel", edad=62, fecha_nacimiento='1959-11-12')
    datos1.save()

    contexto = {
        'datos': datos1,

    }

    return render(request, 'datos.html', contexto)

# Create your views here.
