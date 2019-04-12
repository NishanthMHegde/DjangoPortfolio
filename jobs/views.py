from django.shortcuts import render
from .models import JobModel
# Create your views here.
def home(request):
	jobs = JobModel.objects
	return render(request,'jobs/home.html',{'jobs':jobs})