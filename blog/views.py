from django.shortcuts import render , get_object_or_404
from .models import Post

# Create your views here.

def home(request ):
    # return render(request , 'pages/articles.html')
    # posts = Post.objects.all().order_by('-created_at')
    posts = Post.objects.order_by('-created_at')[:5]  # آخر 5 مقالات فقط

    # return render(request, 'blog/home.html')
    return render(request , 'pages/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'pages/post_detail.html', {'post': post})

def all_posts(request):
    posts = Post.objects.order_by('-created_at')  # كل المقالات
    return render(request, 'pages/all_posts.html', {'posts': posts})
