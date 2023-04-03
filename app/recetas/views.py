# controlador
# recetas/views.py
from django.shortcuts import render
from django.shortcuts import  HttpResponse
from django.shortcuts import  redirect
from .forms import RecetaForm
from .models import Receta
from django.contrib.auth.decorators import login_required, user_passes_test


def busqueda(request):
    q = request.GET.get('q', '')
    nombre = Receta.objects.filter(nombre = q)
    return render(request, 'busqueda.html', {'nombre':nombre})

def index(request):
    receta_list = Receta.objects.all()
    context = {'object_list' : receta_list}
    return render (request, "index.html", context)

def index_oscuro(request):
    response = render(request, 'index_oscuro.html')
    #responde.set_cookie('SESSION_EXPIRE_AT_BROWSER_CLOSE', True)
    return response

@user_passes_test(lambda u: u.is_superuser)
def añadir(request):
    if request.method == 'POST':
        receta = Receta()
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta.nombre = form.cleaned_data['nombre']
            receta.preparación = form.cleaned_data['preparación']
            receta.foto = form.cleaned_data['foto']
            receta.save()
            return redirect(confirmacion)
    else:
        form = RecetaForm()
        context = {'form': form}
    return render(request, 'añadir.html', context)

@login_required
def editar(request, id_receta):
    receta = Receta.objects.get(id=id_receta)
    form = RecetaForm(instance=receta)
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            receta.nombre = form.cleaned_data['nombre']
            receta.preparación = form.cleaned_data['preparación']
            receta.foto = form.cleaned_data['foto']
            receta.save()
        return redirect(confirmacion)

    context = {'form':form}
    return render(request, 'editar.html', context)

@user_passes_test(lambda u: u.is_superuser)
def eliminar(request, id_receta):
	receta = Receta.objects.get(id=id_receta)
	if request.method == 'POST':
		receta.delete()
		return redirect(confirmacion)

	context = {'receta': receta}
	return render(request, 'eliminar.html', context)

def confirmacion(request):
    return render(request, 'confirmacion.html')

def receta(request, nombre_receta):
    receta_unica = Receta.objects.filter(nombre = nombre_receta)
    return render(request, 'receta.html', {'receta_unica':receta_unica})
