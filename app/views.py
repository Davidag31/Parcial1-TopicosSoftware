from django.shortcuts import render, redirect
from .models import Vuelo
from .forms import VueloForm

def inicio(request):
    return render(request, 'index.html')

def registrar_vuelos(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vuelocreado')
    else:
        form = VueloForm()
    return render(request, 'registrar.html', {'form': form})

def listar_vuelos(request):
    vuelos = Vuelo.objects.all()
    return render(request, 'listar.html', {'vuelos': vuelos})

from django.db.models import Avg

def estadisticas_vuelos(request):
    vuelos_nacionales = Vuelo.objects.filter(tipo='Nacional')
    vuelos_internacionales = Vuelo.objects.filter(tipo='Internacional').count()
    estadisticas = f"{vuelos_nacionales.count()} Nacionales, {vuelos_internacionales} Internacionales"
    precio_promedio_nacionales = vuelos_nacionales.aggregate(Avg('precio'))['precio__avg']
    return render(request, 'estadisticas.html', {'estadisticas': estadisticas, 'precio_promedio_nacionales': precio_promedio_nacionales})

def vuelo_creado(request):
    return render(request, 'vuelocreado.html')
