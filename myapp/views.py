from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Proyecto, Lista, Tarea
from .forms import ProyectoForm, ListaForm, TareaForm
from django.views.generic.edit import UpdateView , DeleteView 
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required


def about(request):
    return render(request, "about.html")


@login_required
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

@login_required
def crear_tarea(request):
    form = TareaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "tarea_form.html", {"form": form})

def ver_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    return render(request, "ver-tarea.html", {"tarea": tarea})


class EditarTarea(UpdateView):
    model = Tarea
    template_name = "editar-tarea.html"
    fields = ["titulo", "descripcion", "completada"]
    success_url = reverse_lazy("home")
    pk_url_kwarg = "tarea_id"

class EliminarTarea(DeleteView):
    model = Tarea
    template_name = "eliminar-tarea.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = "tarea_id"

class TareaCompletada (View):
    def post(self, request, id):
        tarea = get_object_or_404(Tarea, id=id)
        tarea.completada = not tarea.completada
        tarea.save()
        return redirect('home')