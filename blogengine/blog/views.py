from django.core import paginator
from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.shortcuts import reverse

from blog.forms import TagForm, PostForm
from .models import Post, Tag
from django.views.generic import View
from .utils import DetailObjectMixin, CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
#def index(request):
    #n = 'Bob'
    #animals = ['Zebra', 'Cat', 'Dog']
    #return HttpResponse('<h1>Hello World (from blog.index)</h1>')
    #return render(request, 'blog/index.html', context= {'animals': animals})
    #return render(request, 'blog/index.html')

def posts_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains = search_query)|Q(body__icontains = search_query))
    else:
        posts=Post.objects.all()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''
    return render(request, 'blog/posts_list.html', context={'page': page, 'next_page_url': next_url, 'prev_page_url': prev_url})

def tags_list(request):
    tags=Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

class PostDetail(DetailObjectMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class TagDetail(DetailObjectMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

class TagCreate(LoginRequiredMixin, CreateObjectMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True
    
class PostCreate(LoginRequiredMixin, CreateObjectMixin, View):
    form = PostForm
    template = 'blog/post_create.html'
    raise_exception = True

class TagUpdate(LoginRequiredMixin, UpdateObjectMixin, View):
    model = Tag
    template = 'blog/tag_update.html'
    form_class = TagForm
    raise_exception = True
    
class PostUpdate(LoginRequiredMixin, UpdateObjectMixin, View):
    model = Post
    template = 'blog/post_update.html'
    form_class = PostForm
    raise_exception = True

class TagDelete(LoginRequiredMixin, DeleteObjectMixin, View):
    model= Tag
    template='blog/tag_delete.html'
    redirect_url='tags_list_url'
    raise_exception = True

class PostDelete(LoginRequiredMixin, DeleteObjectMixin, View):
    model= Post
    template='blog/post_delete.html'
    redirect_url='posts_list_url'
    raise_exception = True

    

