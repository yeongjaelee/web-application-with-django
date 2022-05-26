from .form import ImageForm
from django import views
from django.shortcuts import render,redirect
from .models import Category,Post,Image
from django.views import generic



# Create your views here.
def Image_index(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"lisbon.html",{"obj":obj})
    else:
        form=ImageForm()
    img=Image.objects.all()
    return render(request,"lisbon.html",{"img":img,"form":form})

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

