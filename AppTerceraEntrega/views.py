from django.http import HttpResponse
from django.shortcuts import render
from .models import Empleado

# Create your views here.

def empleado(req, nombre, apellido, email, celular):
    
    empleado = Empleado(nombre=nombre, apellido=apellido, email=email, celular=celular)
    empleado.save()
    
    return HttpResponse(f"""
                        <p>Empleado: {empleado.nombre} {empleado.apellido} agregado!</p>
    """)
    
def lista_empleados(req):
    
    lista = Empleado.objects.all()
    
    return render(req, "lista_empleados.html", {"lista_empleados": lista})