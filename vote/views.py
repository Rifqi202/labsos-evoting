from django.shortcuts import render

from .models import Vote
# Create your views here.
def index(req):
    vote = Vote.object.all()