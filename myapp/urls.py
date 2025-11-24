from django.urls import path
from . import views 
from .views import EditarTarea  , EliminarTarea , TareaCompletada 

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('tarea/', views.crear_tarea, name='crear_tarea'),
    path("tarea/<int:tarea_id>/", views.ver_tarea, name="ver_tarea"),   
    path("tarea/toggle/<int:id>/", TareaCompletada.as_view(), name="toggle_tarea"),
    path("editar-tarea/<int:tarea_id>/", EditarTarea.as_view(), name="editar_tarea"), 
    path("eliminar-tarea/<int:tarea_id>/", EliminarTarea.as_view(), name="eliminar_tarea"),
]
