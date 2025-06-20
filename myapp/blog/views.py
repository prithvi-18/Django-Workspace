from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    blog_title = "Lastest post coming soon"
    posts = [
        {'id':1,'title': 'Post 1', 'content': 'Content of post 1'},
        {'id':2,'title': 'Post 2', 'content': 'Content of post 2'},
        {'id':3,'title': 'Post 3', 'content': 'Content of post 3'},
        {'id':4,'title': 'post 4', 'content': 'content of post 4'},
        {'id':5,'title': 'post 5', 'content': 'content of post 5'},
        {'id':6,'title': 'post 6', 'content': 'content of post 6'},
       ]

    return render(request, 'blog/index.html', {'blog_title': blog_title, 'posts': posts})

def detail(request, post_id):
     return render(request, 'blog/detail.html', {'post_id': post_id})

def old_urls_redrict(request):
    return redirect(reverse('blog:new_page_urls'))


def new_urls_view(request):
    return HttpResponse("This is the new URL view after redirection.")

