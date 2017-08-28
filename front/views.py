from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider,FeaturedImage,LatestBlog
from django.template import Context


# Create your views here.

def index(request):
	context = dict()
	context['sliders'] = Slider.objects.all()
	context['featuredimage'] = FeaturedImage.objects.all()
	context['latestblog'] = LatestBlog.objects.all()
	return render(request, 'index.html', context)
	
def detail(request,blog_id):
	latestblog = LatestBlog.objects.get(pk=blog_id)
	return render(request, 'details.html', {'latestblog': latestblog})
