from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostDemoMainPage(models.Model):
    title = models.CharField(blank=True, null=True, max_length=255)
    description = models.CharField(blank=True, null=True, max_length=400)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images_posts", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
