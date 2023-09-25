from django.shortcuts import render,HttpResponse
from home.models import Post

# Create your views here.
def home(request):
    allpost=Post.objects.all()
    context={
        "allpost":allpost
    }
    return render(request,"home/home.html",context)


def blogpost(request,slug):
    posts = Post.objects.filter(slug=slug).first()
    allpost =Post.objects.all()
    params={
        "posts":posts,
        "allpost":allpost
    }
    return render(request,"home/blogpost.html",params)

