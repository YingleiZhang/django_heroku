from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
	url(r'^$', views.BlogIndex.as_view(), name="index"),
	url(r'^userauth', views.userauth, name="userauth"),
	url(r'^feed/$', views.BlogFeed.as_view(), name="feed"),
	url(r'^post/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="post_detail"),
]
