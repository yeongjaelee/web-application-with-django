from django.contrib import admin
from .models import Category,Post,Image

# Register your models here.

admin.site.register(Image)
admin.site.register(Post)
admin.site.register(Category)
