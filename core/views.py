from django.shortcuts import render
from core.models import AboutMe
from post.models import PostDemoMainPage
# Create your views here.

def index(request):
    details = AboutMe.objects.all()
    posts = PostDemoMainPage.objects.all()
    return render(request, 'core/index.html',{
        'posts':posts,
        'details':details,
    })