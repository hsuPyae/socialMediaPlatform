from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag

# Create your views here.
#def index(request):
    #n = 'Bob'
    #animals = ['Zebra', 'Cat', 'Dog']
    #return HttpResponse('<h1>Hello World (from blog.index)</h1>')
    #return render(request, 'blog/index.html', context= {'animals': animals})
    #return render(request, 'blog/index.html')

def posts_list(request):
    posts=Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts': posts})

def post_detail(request, slug):
    post=Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})

def tags_list(request):
    tags=Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})