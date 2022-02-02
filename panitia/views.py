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
    form = KandidatForm()
    if request.POST:
        form = KandidatForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listkandidat')
    context = {'form': form}
    datakandidat = models.Daftarkandidat.objects.all()
    return render(request, 'daftarkandidat.html',{
        "data": datakandidat,
        'form': form,
    })

def tambahkandidat(request):
    form = KandidatForm()
    if request.POST:
        form = KandidatForm(request.POST)
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
    vote = VoteForm()
    if request.POST:
        vote = VoteForm(request.POST)
        if vote.is_valid():
            vote.save()
        # return redirect('testing')
    context = {'form': vote}
    return render(request, 'tes/tes.html', context)