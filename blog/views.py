from django.shortcuts import render

# Create your views here.

def allblog(request):
	return render(request,'blog/allblog.html')