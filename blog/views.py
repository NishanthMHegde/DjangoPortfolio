from django.shortcuts import render
from .models import BlogModel
# Create your views here.

def allblog(request):
	blogs = BlogModel.objects
	return render(request,'blog/allblog.html', {'blogs' : blogs})