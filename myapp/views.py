from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proyecto, Lista, Tarea
from .forms import ProyectoForm, ListaForm, TareaForm


def home(request):
    proyectos = Proyecto.objects.all()
    listas = Lista.objects.all()

    proyecto_form = ProyectoForm(request.POST or None, prefix='proyecto')
    lista_form = ListaForm(request.POST or None, prefix='lista')

    if request.method == 'POST':
        # Guardar proyecto
        if 'guardar_proyecto' in request.POST and proyecto_form.is_valid():
            proyecto_form.save()
            return redirect('home')

        # Guardar lista
        elif 'guardar_lista' in request.POST and lista_form.is_valid():
            lista_form.save()
            return redirect('home')

    return render(request, "home.html", {
        "proyectos": proyectos,
        "listas": listas,
        "proyecto_form": proyecto_form,
        "lista_form": lista_form,
    })


def crear_tarea(request):
    form = TareaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "tarea_form.html", {"form": form})



   
