from django.shortcuts import render
from .models import Post
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    posts=Post.objects.all()
    return render(request, 'dashboard.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        post = Post(title=title, content=content, image=image)
        post.save()
        messages.success(request, 'Post created successfully!')
        return render(request, 'create_post.html', {'success': True})
    return render(request, 'create_post.html')

def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'view_post.html', {'post': post})