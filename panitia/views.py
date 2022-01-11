from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect

# Create your views here.

def dash(request):
    return render(request, 'dash.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def daftarkandidat(request):
    return render(request, 'daftarkandidat.html')

def datapemilih(request):
    return render(request, 'datapemilih.html')

def datavoting(request):
    return render(request, 'datavoting.html')

def tambahpanitia(request):
    return render(request, 'tambahpanitia.html')

