from django.shortcuts import render, redirect
from .models import Socio
from .forms import SocioForm


def index(request):
    context = {
        'nombre': 'Felipe Alvarez',
        'rut': '19478868-1',
        'seccion': 'Programación Back End (IEI-171-N4)'
    }
    return render(request, 'index.html', context)

def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'lista_socios.html', {'socios': socios})

def agregar_socio(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_socios')
    else:
        form = SocioForm()
    return render(request, 'agregar_socio.html', {'form': form})

def editar_socio(request, pk):
    socio = Socio.objects.get(id=pk)
    if request.method == "POST":
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('lista_socios')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'editar_socio.html', {'form': form})

def eliminar_socio(request, pk):
    Socio.objects.get(id=pk).delete()
    return redirect('lista_socios')
