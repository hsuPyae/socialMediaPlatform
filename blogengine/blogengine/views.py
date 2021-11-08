from django.shortcuts import redirect
"""
from django.http import HttpResponse
def hello(request):
    return HttpResponse('<h1>Hello World</h1>')
    """

def redirect_blog(request):
    return redirect('posts_list_url', permanent=True)
