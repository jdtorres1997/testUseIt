from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('empresa:gestion')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

@login_required
def gestion_usuarios(request):
    usuario = request.user
    if usuario.is_superuser:
        return render(request, 'registration/gestion.html',
                        {'usuarios': User.objects.all()})
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('empresa:gestion')

@login_required
def detail_usuario(request, id_usuario):
    usuario_object = User.objects.get(id=id_usuario)
    usuario = request.user
    if usuario_object.id == usuario.id or usuario.is_superuser:
        return render(request, 'registration/detail.html', {'usuario': usuario_object})
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('empresa:gestion')