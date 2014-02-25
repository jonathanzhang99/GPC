from django.shortcuts import render
from home.models import member
from django.http import HttpResponse

def index(request):
    return render(request, 'home\\index.html')
