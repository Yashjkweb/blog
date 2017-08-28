from django.db import models
from django.utils import timezone

# Create your models here.
class Slider(models.Model):
	imageslider = models.ImageField(upload_to='media')
	
class FeaturedImage(models.Model):
	featuredimage = models.ImageField(upload_to='media')

class LatestBlog(models.Model):
	PostedBy = models.CharField(max_length=100)
	BlogTitle = models.CharField(max_length=200)
	BlogDescription = models.TextField()
	BlogImage = models.ImageField(upload_to='media')
	created_date = models.DateTimeField(default=timezone.now)
	
