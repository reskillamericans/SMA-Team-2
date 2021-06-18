from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages #import messages
from .models import User

# Create your views here.

def index(request):
    #return HttpResponse("Welcome, this is the SMA app")
	return render (request=request, template_name="home.html")

def register_request(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		confirmpwd = request.POST['conf_password']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		
		if password == confirmpwd:
			try:
				user = User.objects.get(email=email)
				messages.error(request, "Email already exists")
				return redirect("register")
			except User.DoesNotExist:
				user = User.objects.create_user(email=email, username=username, password=password, first_name=first_name, last_name=last_name)
				user.save()
				messages.success(request, "Registration successful")
				return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	return render(request=request, template_name="register.html")