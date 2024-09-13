from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrar/', views.registrar_vuelos, name='registrar'),
    path('listar/', views.listar_vuelos, name='listar'),
    path('estadisticas/', views.estadisticas_vuelos, name='estadisticas'),
     path('vuelocreado/', views.vuelo_creado, name='vuelocreado'),
]

