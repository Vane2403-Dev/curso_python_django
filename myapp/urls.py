from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tarea/', views.crear_tarea, name='crear_tarea'),
]
