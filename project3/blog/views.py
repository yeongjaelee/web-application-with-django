from django.shortcuts import render
from blog.models import Category,Post
from django.views import generic

# Create your views here.

def index(req):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        "post_latest" : post_latest
    }
    return render(req,"index.html", context=context)

def about(req):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        "post_latest" : post_latest
    }
    return render(req,"about.html",context=context)

def lisbon(req):
    context = {

    }
    return render(req,"lisbon.html",context=context)

def skills(req):
    context = {

    }
    return render(req,"skills.html",context=context)

def contact(req):
    context = {

    }
    return render(req,"contact.html",context=context)
class PostDetailView(generic.DetailView):
    model = Post

