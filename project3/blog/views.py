from .form import ImageForm
from django import views
from django.shortcuts import render,redirect
from .models import Category,Post,Image
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import auth

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

def login(req):
    if req.method=="POST":
        username = req.POST["username"]
        password = req.POST["password"]
        user = auth.authenticate(req, username=username, password=password)
        if user is not None:
            auth.login(req,user)
            return redirect("index")
        else:
            return render(req,"login.html",{'error':'username or password is incorrect'})
    
    else:
        return render(req,'login.html')

def logout(req):
    auth.logout(req)
    return redirect("index")

def signup(req):
    if req.method =="POST":
        if req.POST["password1"] == req.POST["password2"]:
            user = User.objects.create_user(
                username = req.POST["username"], password = req.POST["password1"])
            auth.login(req,user)
        return render(req,'signup.html')
    
    return render(req,'signup.html')

                
class PostDetailView(generic.DetailView):
    model = Post

