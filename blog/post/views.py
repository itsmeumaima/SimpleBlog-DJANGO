from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    posts=Post.objects.all()
    return render(request, 'dashboard.html', {'posts': posts})