from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('vote/<kandidat_id>', views.vote, name='vote'),
    path('hasilvoting/', views.hasilvoting),
]