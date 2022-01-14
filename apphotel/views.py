from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Local, Locador, Reserva
from .forms import LocadorForm, LocalForm, ReservaForm

@login_required()
def index(request):
    lista_local = Local.objects.all()

    search = request.GET.get('search')

    if search:

        lista_local = Local.objects.filter(title_icontains=search)

    else:
        return render(request, 'home.html', {
            'lista_local': lista_local
        })

    return render(request, 'home.html', {
        'lista_local': lista_local
    })

def reservar_local(request):
    form_reserva = ReservaForm(request.POST or None)

    if form_reserva.is_valid():
        form_reserva.save()
        return redirect('apphotel:index')

    return render(request, 'confirmar_reserva.html', {
        'form_reserva': form_reserva
    })

def admin_edit(request):
    return render(request, 'administrador.html')

@login_required()
def create_locador(request):
    form_locador = LocadorForm(request.POST or None)

    if form_locador.is_valid():
        form_locador.save()
        return redirect('apphotel:index')

    return render(request, 'locador.html', {
        'form_locador': form_locador
    })

@login_required()
def create_local(request):
    form_local = LocalForm(request.POST or None)

    if form_local.is_valid():
        form_local.save()
        return redirect('apphotel:index')

    return render(request, 'local.html', {
        'form_local': form_local
    })

def delete_local(request, id):
    local_delete = Local.objects.get(id=id)

    if request.method == 'POST':
        local_delete.delete()
        return redirect('apphotel:index')

    return render(request, 'delete_local.html', {
        'local_delete': local_delete
    })

def delete_locador(request, id):
    locador_delete = Locador.objects.get(id=id)

    if request.method == 'POST':
        locador_delete.delete()
        return redirect('apphotel:index')

    return render(request, 'locador_delete.html', {
        'locador_delete': locador_delete
    })

def select_locador(request):
    lista_locador = Locador.objects.all()

    return render(request, 'selecionar_locador.html', {
        'lista_locador': lista_locador
    })
