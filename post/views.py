from django.shortcuts import render
from .models import PostDemoMainPage
# Create your views here.

def PostView(request, id):
    PostID = PostDemoMainPage.objects.get(id=id)
    return render (request ,'post/post.html',{
        # 'postDetail':postDetail,
        'PostId':PostID,
        })
