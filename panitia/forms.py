from django import forms
from django.forms import ModelForm
from django import forms
from .models import Daftarkandidat, judul

class KandidatForm(ModelForm):
	class Meta:
		model = Daftarkandidat
		exclude = []


class judulpemilihan(ModelForm):
	class Meta:
		model = judul
		fields = ['judul']

    