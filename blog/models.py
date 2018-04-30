from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	"""这里是分类"""
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Tag(models.Model):
	"""这里是标签"""
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Post(models.Model):
	"""这里是文章"""
	title = models.CharField(max_length=70)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	excerpt = models.CharField(max_length=200)
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag,blank=True)
	aythor = models.ForeignKey(User)
	def __str__(self):
		return self.title
	def get_absolute_url(self):#为Post生成自已的url
		return reverse('blog:detail',kwargs={'pk':self.pk})
	class Meta:
		ordering = ['-created_time']