from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash, name= 'dash'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('daftarkandidat/', views.daftarkandidat, name='daftarkandidat'),
    path('datapemilih/', views.datapemilih, name= 'datapemilih'),
    path('datavoting/', views.datavoting, name= 'datavoting'),
    path('tambahpanitia/', views.tambahpanitia, name= 'tambahpanitia'),
]