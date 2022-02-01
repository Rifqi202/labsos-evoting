<<<<<<< HEAD
from django.forms import ModelForm
from .models import Daftarkandidat, Vote
=======
from django import forms
from django.forms import ModelForm
from django import forms
from .models import Daftarkandidat, judul
>>>>>>> deac0a38b8885085be6191a61a897d6739eccde6

class KandidatForm(ModelForm):
	class Meta:
		model = Daftarkandidat
		exclude = []


class VoteForm(ModelForm):
	class Meta:
		model = Vote
		fields = '__all__'

    