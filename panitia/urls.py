from django.urls import path
from . import views


urlpatterns = [
    path('', views.dash, name= 'dash'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('daftarkandidat/', views.daftarkandidat, name='daftarkandidat'),
    path('tambahkandidat/', views.tambahkandidat, name = 'tambahkandidat'),
    path('detailprofil/<id>', views.detailprofil, name = 'detailprofil'),
    path('detailprofil/<id>/delete', views.delete, name = 'delete'),
    path('editkandidat/<id>/edit', views.editkandidat, name = 'editkandidat'),
    # path('delete/<id>', views.delete, name = 'delete'),
    path('datapemilih/', views.datapemilih, name = 'datapemilih'),
    path('datavoting/', views.datavoting, name = 'datavoting'),
    path('tambahpanitia/', views.tambahpanitia, name = 'tambahpanitia'),
]