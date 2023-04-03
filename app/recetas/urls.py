# recetas/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busqueda', views.busqueda, name='busqueda'),
    path('index_oscuro', views.index_oscuro, name='index_oscuro'),
    path('añadir', views.añadir, name='añadir'),
    path('eliminar/<str:id_receta>/', views.eliminar, name='eliminar'),
    path('editar/<str:id_receta>/', views.editar, name='editar'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('receta/<str:nombre_receta>/', views.receta, name='receta'),
]