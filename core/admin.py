from django.contrib import admin
from .models import AboutMe
from post.models import PostDemoMainPage
# Register your models here.

admin.site.register(AboutMe)
admin.site.register(PostDemoMainPage)