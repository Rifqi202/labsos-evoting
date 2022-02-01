# # forms.py
# from pyexpat import model
from django.forms import ModelForm
from .models import daftarkandidat, judul

class KandidatForm(ModelForm):
	class Meta:
		model = daftarkandidat
		fields = '__all__'


class judulpemilihan(ModelForm):
	class Meta:
		model = judul
		fields = ['judul']

    