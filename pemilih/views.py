from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from panitia import models as panitiamodels
from .models import Vote
# Create your views here.

# @method_decorator(login_required, name='dispatch')
@login_required
def index(request):
    kandidat = panitiamodels.Daftarkandidat.objects.all()
    print(kandidat)
    return render(request, 'voting.html', {'kandidat': kandidat})

# @method_decorator(login_required)
@login_required
def vote(request, kandidat_id):
    # judul = panitiamodels.judul.objects.all()
    kandidatbyid = panitiamodels.Daftarkandidat.objects.get(pk=kandidat_id)
    Vote.objects.create(kandidat=kandidatbyid)
    messages.info(request, f'yeeeeeeeeeeeeha, hakdes hakdeds | Vote Berhasil | uhuyyyyy josss')
    return redirect('/')

# @method_decorator(login_required)
@login_required
def hasilvoting(request):
    return render(request, 'hasilvoting.html')