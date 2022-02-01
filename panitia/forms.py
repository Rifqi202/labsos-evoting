from django import forms
from django.forms import CharField, DateInput, ModelForm
from .models import Daftarkandidat, judul

class KandidatForm(ModelForm):
	tanggallahir = forms.CharField(
		widget=forms.DateInput(attrs={'type': 'date'})
	)
	class Meta:
		model = Daftarkandidat
		exclude = ['kandidat_Main_Img']


class judulpemilihan(ModelForm):
	class Meta:
		model = judul
		fields = ['judul']

    