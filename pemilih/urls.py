from django.urls import path
from . import views

urlpatterns = [
    path('dashboard2/', views.dashboard2, name='dashboard2'),
    path('', views.voting, name= 'voting'),
    path('hasilvoting/', views.hasilvoting, name='hasilvoting'),
]