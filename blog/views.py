from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from . import models

# Create your views here.
class BlogLogin(generic.ListView):
	model = User
	template_name = "blog/login.html"

class BlogFeed(generic.ListView):
	queryset = models.Post.objects.published()[:5]
	template_name = "blog/feed.html"

class BlogIndex(generic.ListView):
	queryset = models.Post.objects.published()
	template_name = "blog/home.html"

class BlogDetail(generic.DetailView):
	model = models.Post
	template_name = "blog/post.html"

