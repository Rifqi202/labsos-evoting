
from django.forms import ModelForm
from .models import Daftarkandidat, Vote
from django import forms


class KandidatForm(ModelForm):
	tanggallahir = forms.CharField(
		widget=forms.DateInput(attrs={'type': 'date'})
	)
	class Meta:
		model = Daftarkandidat

		fields = '__all__'
		exclude = ['kandidat_Main_Img']

class VoteForm(ModelForm):
	Waktu = forms.CharField(
		widget=forms.DateInput(attrs={'type': 'date'})
	)
	class Meta:
		model = Vote
		fields = '__all__'

    