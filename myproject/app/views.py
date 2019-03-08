from django.shortcuts import render
from .models import user

def home(request):
	data=user.objects.all()
	context={
	'data':data
	}
	return render(request,"app/home.html",context)
	