from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    panitia = models.BooleanField('panitia', default=False)
    pemilih = models.BooleanField('pemilih', default=False)
    # is_employee = models.BooleanField('Is employee', default=False)

    def __str__(self):
        return self.username

class Pemilih(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='usernames')
    nim = models.IntegerField()
    prodi = models.CharField(max_length=26, default='')

    def __str__(self):
        return self.username

# class Anggota(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     pemilih = models.ForeignKey(Pemilih, on_delete=models.CASCADE)