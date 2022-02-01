from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.dash, name= 'dash'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('listkandidat/', views.listkandidat, name='listkandidat'),
    path('tambahkandidat/', views.tambahkandidat, name = 'tambahkandidat'),
    path('detailprofil/<id>', views.detailprofil, name = 'detailprofil'),
    path('<id>/delete', views.delete, name = 'delete'),
    path('editkandidat/<id>/edit', views.editkandidat, name = 'editkandidat'),
    # path('judul/', views.judul, name = 'judul'),
    path('datapemilih/', views.datapemilih, name = 'datapemilih'),
    path('datavoting/', views.datavoting, name = 'datavoting'),
    # path('tambahpanitia/', views.tambahpanitia, name = 'tambahpanitia'),
    path ('testing/', views.testing)
]