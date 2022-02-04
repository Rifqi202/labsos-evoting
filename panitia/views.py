from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import models, forms
from accounts import models as accountsmodels
from pemilih import models as pemilihmodels
# from .forms import KandidatForm, VoteForm

# Create your views here.
@login_required
def dash(request):
    form = forms.VoteForm()
    if request.POST:
        form = forms.VoteForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect ('dash')

    # judul = models.judul.objects.all()
    return render(request, 'dash.html',{
        'form': form,
       
    })

def dashboard(request):
    return render(request, 'dashboard.html')

# @login_requireds
def listkandidat(req):
    form = forms.KandidatForm()
    if req.POST:
        form = forms.KandidatForm(req.POST)
        if form.is_valid():
            form.save()
            # return redirect('listkandidat')
        
    datakandidat = models.Daftarkandidat.objects.all()
    print(datakandidat)
    return render(req, 'daftarkandidat.html',{
        'data': datakandidat,
        'form': form,
    })

def tambahkandidat(request):
    form = forms.KandidatForm()
    if request.POST:
        form = forms.KandidatForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listkandidat')
    context = {'form': form}
    return render(request, 'tambahkandidat.html', context)

# @login_required
def detailprofil(request, id):
    detailprofil = models.Daftarkandidat.objects.filter(id = id).first()
    return render(request, 'detailprofil.html', {
        'data': detailprofil,
    })

# @login_required
def editkandidat(request, id):
    if request.POST:
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

# @login_required
def delete(request, id):
    models.Daftarkandidat.objects.filter(id = id).delete()
    return redirect('/panitia/listkandidat')


def datapemilih(request):
    return render(request, 'datapemilih.html')

def hasil(request):
    hasil_vote = pemilihmodels.Vote.objects.all()
    return render(request, 'hasilvote.html', {'hasil': hasil_vote})

def detailprofil(request):
    return render(request, 'detailprofil.html')

def datapemilih(request):
    pemilih = accountsmodels.User.objects.all()
    return render(request, 'datapemilih.html',{
        'pemilih': pemilih
    })
def testing(request):
    vote = forms.VoteForm()
    if request.POST:
        vote = forms.VoteForm(request.POST)
        if vote.is_valid():
            vote.save()
        # return redirect('testing')
    judul = models.Vote.objects.all()
    context = {'form': vote, 'data': judul,}
    return render(request, 'tes/tes.html', context)
    # return render(request, 'tes/tes.html')
    
def tambahvote(request):
    vote = forms.VoteForm()
    if request.POST:
        vote = forms.VoteForm(request.POST)
        if vote.is_valid():
            vote.save()
        # return redirect('testing')
    context = {'form': vote}
    return render(request, 'tes/tes.html', context)
