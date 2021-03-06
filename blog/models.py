from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.slug

class PostQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	tags = models.ManyToManyField(Tag)

	objects = PostQuerySet.as_manager()

	def get_absolute_url(self):
		return reverse("blog:post_detail", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Blog Post"
		verbose_name_plural = "Blog Posts"
		ordering = ["-created"]


