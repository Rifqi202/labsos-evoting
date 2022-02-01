from django.db import models
from panitia import models as panitia_models

# Create your models here.
class Vote(models.Model):
    kandidat = models.ForeignKey(panitia_models.Daftarkandidat, on_delete=models.CASCADE, related_name='pilihan')

    def __str__(self):
        return self.kandidat.namakandidat