from django.forms import ModelForm
from .models import Daftarkandidat, Vote

class KandidatForm(ModelForm):
	class Meta:
		model = Daftarkandidat
		fields = '__all__'


class VoteForm(ModelForm):
	class Meta:
		model = Vote
		fields = '__all__'

    