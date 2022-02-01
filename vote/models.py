from django.db import models
from panitia import models as panitiamodels
from accounts import models as accountmodels
# Create your models here.

class Vote(models.Model):
    pemilih = models.ForeignKey(accountmodels.User, on_delete=models.CASCADE)
    kandidat = models.ForeignKey(panitiamodels.Daftarkandidat, on_delete=models.CASCADE, related_name='pilih')

    def __str__(self):
        return self.kandidat.namakandidat, self.kandidat.nomerurut