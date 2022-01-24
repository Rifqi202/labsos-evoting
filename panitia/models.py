from django.db import models

# Create your models here.



class daftarkandidat(models.Model):
    namakandidat = models.TextField(max_length=100, default='')
    nomerurut = models.IntegerField(default='')
    tempatlahir = models.TextField(max_length=100, default='')
    tanggallahir = models.DateField()
    alamat = models.TextField(max_length=100, default='')
    pengalaman = models.TextField(max_length=100, default='')
    prestasi = models.TextField(max_length=100, default='')
    visi = models.TextField(max_length=100, default='')
    misi = models.TextField(max_length=100, default='')
    programkerja = models.TextField(max_length=100, default='')
    kandidat_Main_Img = models.ImageField (upload_to='images/')


class judul(models.Model):
    judul = models.TextField(default='')
