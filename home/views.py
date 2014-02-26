from django.shortcuts import render
from home.models import Member, Post
from django.shortcuts import get_list_or_404
from django.utils import timezone
from django.http import HttpResponse

def index(request):
#    general = get_list_or_404(Post, pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(request, 'home\index.html')

def python(request):
    return render(request, "home\python.html")
