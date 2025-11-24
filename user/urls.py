from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_view, name='ingresar'),
    path('registro/', views.crear_usuario, name='registro'),
    path ('cerrar-sesion/', LogoutView.as_view (template_name = 'cerrar_sesion.html'), name = 'cerrar_sesion')
]
