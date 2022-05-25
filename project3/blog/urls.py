from django.urls import URLPattern, re_path,path
from . import views
from blog import views

urlpatterns =[
    path("",views.index, name="index"),
    path("about/",views.about,name="about"),
    path("lisbon/",views.lisbon,name="lisbon"),
    path("skills/",views.skills,name="skills"),
    path("contact/",views.contact,name="contact"),
    path("post/<int:pk>",views.PostDetailView.as_view(),name="post")
]