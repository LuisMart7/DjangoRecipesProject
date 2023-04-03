# mi_sitio/urls.py
from django.contrib import admin
from django.urls import path, include
  
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('recetas.urls')),
]

