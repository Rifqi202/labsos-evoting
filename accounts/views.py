from django.shortcuts import render, redirect
from .forms import SignUpAdminForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpAdminForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('/')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpAdminForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.panitia:
                login(request, user)
                return redirect('/panitia')
            elif user is not None and user.pemilih:
                login(request, user)
                return redirect('/pemilih')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def logout_user(request):
    logout(request)
    return redirect('/')