from django.shortcuts import render, redirect
from Socios_APP.models import Socio
from Socios_APP.forms import SocioForm


def index(request):
    context = {
        'nombre': 'Felipe Alvarez',
        'rut': '19478868-1',
        'seccion': 'Programación Back End (IEI-171-N4)'
    }
    return render(request, 'index.html', context)

def lista_socios(request):
    socios = Socio.objects.all()
    data = {
        'socio': socios
    }
    return render(request, 'lista_socios.html', data)

def agregar_socio(request):
    form = SocioForm()
    
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar')
    
    data = {
        'form': form
    }
    return render(request, 'agregar_socio.html', data)

def editar_socio(request, pk):
    socio = Socio.objects.get(id=pk)
    form = SocioForm(instance=socio)
    if request.method == "POST":
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('/listar')
    
    data = {
        'form': form
    }
    return render(request, 'editar_socio.html', data)

def eliminar_socio(request, pk):
    if request.method == "POST":
        socio = Socio.objects.get(id=pk)
        socio.delete()
        return redirect('/listar')
    
    else:
        return redirect('/listar')
