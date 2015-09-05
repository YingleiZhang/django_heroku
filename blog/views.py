from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views import generic
from django.contrib.auth.models import User
from . import models

# Create your views here.
def userlogin(request):
	context = RequestContext(request, {'request':request, 'user':request.user})
	return render_to_response('blog/login.html',context_instance=context)
"""
class BlogLogin(generic.ListView):
	model = User
	template_name = "blog/login.html"
"""
class BlogFeed(generic.ListView):
	queryset = models.Post.objects.published()[:5]
	template_name = "blog/feed.html"

class BlogIndex(generic.ListView):
	queryset = models.Post.objects.published()
	template_name = "blog/home.html"

class BlogDetail(generic.DetailView):
	model = models.Post
	template_name = "blog/post.html"

