from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

def crear_usuario(request):
    if request.method == "GET":
        return render(request, "registro.html", {"form": UserCreationForm()})

    # POST
    username = request.POST.get("username")
    p1 = request.POST.get("password1")
    p2 = request.POST.get("password2")

    # Validación de contraseñas
    if p1 != p2:
        return render(
            request,
            "registro.html",
            {"form": UserCreationForm(), "error": "Las contraseñas no coinciden."}
        )

    # Intento de creación de usuario
    try:
        user = User.objects.create_user(username=username, password=p1)
        user.save()

        return redirect("ingresar")

    except IntegrityError:
        return render(
            request,
            "registro.html",
            {"form": UserCreationForm(), "error": "El nombre de usuario ya existe."}
        )

def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "logging.html", {"form": AuthenticationForm()})

    form = AuthenticationForm(request, data=request.POST)

    if not form.is_valid():
        return render(
            request,
            "logging.html",
            {
                "form": form,
                "error": "Usuario o contraseña incorrectos."
            }
        )

    usuario = form.get_user()
    login(request, usuario)
    return redirect("home")