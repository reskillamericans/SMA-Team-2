from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages #import messages
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserSocial
from .forms import UserProfileForm

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




def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()		
	return render(request=request, template_name="login.html")	



def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    UserSocial = user.UserSocial
    form = UserProfileForm(instance=UserSocial)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            form = UserProfileForm(request.POST, request.FILES, instance=UserSocial)

            if form.is_valid():
                update = form.save(commit=False)               
                update.user = user
                update.save()
            return HttpResponse('Confirm')                
    else:
        form = UserProfileForm(instance=UserSocial)

    return render(request=request, template_name="profile.html")	