from django.shortcuts import render, HttpResponse
# from Evoting.panitia.models import judul
from panitia import models as panitiamodels

# Create your views here.

def dashboard2(request):
    return render(request, 'dashboard2.html')

def voting(request):
    judul = panitiamodels.judul.objects.all()
    return render(request, 'voting.html',{
        'judul':judul,
    })

def hasilvoting(request):
    return render(request, 'hasilvoting.html')