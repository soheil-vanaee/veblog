from operator import mod
from django.db import models

# Create your models here.

class AboutMe(models.Model):
    HeaderImage = models.TextField(blank=True, null=True, default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fthumbnails%2F001%2F233%2F908%2Fsmall%2Fmodern-green-overlapping-banner-background.jpg&f=1&nofb=1&ipt=abfd64362b89d2ed7bb0e967e58ebaf5af9df470013d3d3dc64c6f59d22e40f0&ipo=images")
    ProfileImage = models.TextField(blank=True, null=True, default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fblog.alliedmarketresearch.com%2Fimages%2Fuser_icon.png&f=1&nofb=1&ipt=3fa3cccc7873c89c86816feb407f17445fa976943c10f7aff541d36e3ea21bc3&ipo=images")
    Name = models.CharField(blank=True, null=True,max_length=150)
    AboutMe = models.CharField(blank=True, null=True,max_length=450)
    github = models.CharField(blank=True, null=True,max_length=450)
    twitter = models.CharField(blank=True, null=True,max_length=450)
    linkedin = models.CharField(blank=True, null=True,max_length=450)
    insta = models.CharField(blank=True, null=True,max_length=450)