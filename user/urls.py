from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.login_view, name='ingresar'),
    path('registro/', views.crear_usuario, name='registro'),
    path('cerrar-sesion/', LogoutView.as_view(template_name='cerrar_sesion.html'), name='cerrar_sesion'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
]


