from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import models
from accounts import models as accountsmodels
from .forms import *
# from .forms import KandidatForm, VoteForm

# Create your views here.
@login_required
def dash(request):
    form = VoteForm()
    if request.POST:
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect ('dash')

    # judul = models.judul.objects.all()
    return render(request, 'dash.html',{
        'form': form,
       
    })

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def listkandidat(request):
    datakandidat = models.Daftarkandidat.objects.all()
    return render(request, 'daftarkandidat.html',{
        "data": datakandidat,
    })

@login_required
def tambahkandidat(request):
    if request.POST:
        input_namakandidat = request.POST["namakandidat"]
        input_nomerurut = request.POST["nomerurut"]
        input_tempatlahir = request.POST["tempatlahir"]
        input_tanggallahir = request.POST["tanggallahir"]
        input_alamat = request.POST["alamat"]
        input_pengalaman = request.POST["pengalaman"]
        input_prestasi = request.POST["prestasi"]
        input_visi = request.POST["visi"]
        input_misi = request.POST["misi"]
        input_programkerja = request.POST["programkerja"]
        # input_kandidat_Main_Img = request.POST["kandidat_Main_Img"]
        models.Daftarkandidat.objects.create(namakandidat = input_namakandidat, nomerurut = input_nomerurut, tempatlahir = input_tempatlahir, tanggallahir = input_tanggallahir, alamat = input_alamat, pengalaman = input_pengalaman, prestasi = input_prestasi, visi = input_visi, misi = input_misi, programkerja = input_programkerja)
    
    data = models.Daftarkandidat.objects.all()
    return render(request, "daftarkandidat.html",{
        "data": data,
    })

def tambahkandidat(request):
    form = KandidatForm()
    if request.method == 'POST':
        form = KandidatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('listkandidat')
    context = {'form': form}
    return render(request, 'daftarkandidat.html', context)

@login_required
def detailprofil(request, id):
    detailprofil = models.Daftarkandidat.objects.filter(id = id).first()
    return render(request, 'detailprofil.html', {
        'data': detailprofil,
    })

@login_required
def editkandidat(request, id):
    if request.POST:
        
        print(input)
        models.Daftarkandidat.objects.filter(pk = id).update(
        namakandidat = request.POST["namakandidat"],
        nomerurut = request.POST["nomerurut"],
        tempatlahir = request.POST["tempatlahir"],
        tanggallahir = request.POST["tanggallahir"],
        alamat = request.POST["alamat"],
        pengalaman = request.POST["pengalaman"],
        prestasi = request.POST["prestasi"],
        visi = request.POST["visi"],
        misi = request.POST["misi"],
        programkerja = request.POST["programkerja"],
        # input_kandidat_Main_Img = request.POST["kandidat_Main_Img"],
        )
        return redirect('daftarkandidat')

    editkandidat = models.Daftarkandidat.objects.filter(id = id).first()
    return render( request, "editkandidat.html", {
        'data': editkandidat,
    })

@login_required
def delete(request, id):
    models.Daftarkandidat.objects.filter(id = id).delete()
    return redirect('/panitia/daftarkandidat')


def datapemilih(request):
    return render(request, 'datapemilih.html')

def datavoting(request):
    return render(request, 'datavoting.html')

def detailprofil(request):
    return render(request, 'detailprofil.html')

def datapemilih(request):
    pemilih = accountsmodels.User.objects.all()
    return render(request, 'datapemilih.html',{
        'pemilih': pemilih
    })
def testing(request):
    return render(request, 'tes/tes.html')
    
def tambahvote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('testing')
    else:
        form = VoteForm()
        return render(request, 'tes.html', {'form' : form})