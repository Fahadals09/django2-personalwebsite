from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def post_list(request):
    all_posts = Post.objects.all()
    context = {'posts':all_posts}
    return render(request,'blog/post_list.html',context)

def post_detail(request , id):
    post = Post.objects.get(id=id)
    context = {'post' : post}
    return render(request,'blog/post_detail.html',context)

