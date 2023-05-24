from django.shortcuts import render
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    
    print(posts)
    
    return
    
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    
    print(post)
    
    return