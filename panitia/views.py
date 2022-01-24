# from django.forms import Input
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from . import models

# Create your views here.

def dash(request):
    if request.method == 'POST':
        models.judul.objects.create(
            judul = request.POST['judul']
            )
        return redirect ('dash')
    judul = models.judul.objects.all()
    return render(request, 'dash.html',{
        'judul': judul,
    })

def dashboard(request):
    return render(request, 'dashboard.html')

def daftarkandidat(request):
    if request.POST:
        models.daftarkandidat.objects.create(
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
            # kandidat_Main_Img = request.POST["kandidat_Main_Img"]
            )
        return redirect('/panitia/daftarkandidat')
    data = models.daftarkandidat.objects.all()
    return render(request, 'daftarkandidat.html',{
        "data": data,
    })

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
        models.daftarkandidat.objects.create(namakandidat = input_namakandidat, nomerurut = input_nomerurut, tempatlahir = input_tempatlahir, tanggallahir = input_tanggallahir, alamat = input_alamat, pengalaman = input_pengalaman, prestasi = input_prestasi, visi = input_visi, misi = input_misi, programkerja = input_programkerja, kandidat_Main_Img = input_kandidat_Main_Img)
    
    data = models.daftarkandidat.objects.all()
    return render(request, "daftarkandidat.html",{
        "data": data,
    })


def detailprofil(request, id):
    detailprofil = models.daftarkandidat.objects.filter(id = id).first()
    return render(request, 'detailprofil.html', {
        'data': detailprofil,
    })

def editkandidat(request, id):
    if request.POST:
        namakandidat = request.POST["namakandidat"]
        nomerurut = request.POST["nomerurut"]
        tempatlahir = request.POST["tempatlahir"]
        tanggallahir = request.POST["tanggallahir"]
        alamat = request.POST["alamat"]
        pengalaman = request.POST["pengalaman"]
        prestasi = request.POST["prestasi"]
        visi = request.POST["visi"]
        misi = request.POST["misi"]
        programkerja = request.POST["programkerja"]
        input_kandidat_Main_Img = request.POST["kandidat_Main_Img"]
        print(input)
        models.daftarkandidat.objects.filter(id = id).update()
        return redirect('daftarkandidat')

    editkandidat = models.daftarkandidat.objects.filter(id = id).first()
    return render( request, "editkandidat.html", {
        'data': editkandidat,
    })

def delete(request, id):
    models.daftarkandidat.objects.filter(id = id).delete()
    return redirect('/panitia/daftarkandidat')


def datapemilih(request):
    return render(request, 'datapemilih.html')

def datavoting(request):
    return render(request, 'datavoting.html')

def tambahpanitia(request):
    return render(request, 'tambahpanitia.html')

