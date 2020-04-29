from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
def index(request):

    posts = Blogpost.objects.all()
    params = {'myposts':posts}
    return render(request,'blog/index.html',params)

def blogPost(request,id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request,'blog/blogPost.html',{'post':post})