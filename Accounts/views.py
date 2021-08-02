from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages  #import messages
from .models import User, PasswordReset
from Details.models import Follower
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from .models import UserSocial
from .forms import UserProfileForm

from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from Details.models import Post, PostComment

from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    #return HttpResponse("Welcome, this is the SMA app")
	return render (request=request, template_name="home.html")

def register_request(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		confirmpwd = request.POST.get('conf_password')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		
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
	
	if request.user.is_authenticated:
		return redirect("index")

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			messages.info(request, f"You are now logged in as {username}.")
			return redirect("index")
		else:
			messages.error(request,"Invalid username or password.")
			return redirect("login")	
	
	return render(request, "login.html")	


	
def edit_user(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST,instance=UserSocial)
		if form.is_valid():
			form.save()
			messages.success(request,'Your Profile has been updated!')
			return redirect('profile')
	else:
		form = UserProfileForm(instance=UserSocial)
		context = {'form': form}
		return render(request=request, template_name="profile.html", context=context)

	messages.error(request,"Invalid username or password.")	
	return render(request=request, template_name="login.html")	




def password_reset_request(request):
	
	if request.method == "POST":
		email = request.POST['email']
		user = User.objects.filter(email=email).first()

		# Record token in PasswordReset model
		token = default_token_generator.make_token(user)
		passwordResetModel = PasswordReset.objects.create(user_id=user, token=token)
		passwordResetModel.save()

		# Create and send e-mail
		subject = "Password Reset Requested"
		email_template_name = "password_reset_email.txt"
		c = {
			"email": user.email,
			"domain": "127.0.0.1:8000",
			"site_name": "SMA Team 2", 
			"uid": urlsafe_base64_encode(force_bytes(user.pk)),
			"user": user,
			"token": token,
			"protocol": "http",
		}

		email = render_to_string(email_template_name, c)
		try:
			send_mail(subject, email, "team2@sma.com", [user.email], fail_silently=False)
		except BadHeaderError:
			return HttpResponse("Invalid header found.")
		return redirect("password_reset_done")
	
	return render(request=request, template_name="password_reset.html")


def password_reset_done_request(request):
	return render(request=request, template_name="password_reset_done.html")


def password_reset_confirm_request(request, uidb64, token):
	user_id = force_text(urlsafe_base64_decode(uidb64))
	user = User.objects.filter(id=user_id).first()

	if request.method == "POST":
		password = request.POST['password']
		confirmpwd = request.POST['conf_password']
		
		if password == confirmpwd:
			user.set_password(password)
			user.save()
			
			passwordResetModel = PasswordReset.objects.filter(user_id=user, token=token).first()
			passwordResetModel.token_used = True
			passwordResetModel.save()

			return render(request=request, template_name="password_reset_complete.html")
		else:
			messages.error(request, "Passwords do not match.")

	else:
		passwordResetModel = PasswordReset.objects.filter(user_id=user, token=token).first()

		if passwordResetModel.token_used == True:
			return HttpResponse("Token has already been used.")

	return render(request=request, template_name="password_reset_confirm.html")
	
	
def password_reset_complete_request(request):
	return render(request=request, template_name="password_reset_complete.html")


def post_comment_request(request, pk):
	
	try:
		post = Post.objects.get(id=pk)
	except Post.DoesNotExist:
		messages.error("Post does not exist")
		return redirect("index")
		
	if request.method == "POST":
		comment = request.POST['comment']
		session_user = request.user
		user = User.objects.get(email=session_user)
		post_comment = PostComment(commenter_id=user, post_id=post, content=comment)
		post_comment.save()
		messages.success(request, "Comment successfully posted")
		return redirect("index")

	return render(request, "comment.html", {'post':post}) 



def delete_comment(request, id):
   
    comment = get_object_or_404('Comment', id=id)
    try:
        comment.delete()
        messages.success(request, 'You have successfully deleted the comment')

    except:
        messages.warning(request, 'The comment could not be deleted.')
        return redirect("index")







def follow_user(request, user_name):
    other_user = User.objects.get(username=user_name)
	#get id 
    session_user = request.session['user']
    get_user = User.objects.get(username=session_user)
    check_follower = Follower.objects.get(username=get_user.id)
    is_followed = False
    if other_user.username != session_user:
        if check_follower.follower_id.filter(username=other_user).exists():
            add_usr = Follower.objects.get(username=get_user)
            add_usr.follower_id.remove(other_user)
            is_followed = False
            return redirect(f'/profile/{session_user}')
        else:
            add_usr = Follower.objects.get(username=get_user)
            add_usr.follower_id.add(other_user)
            is_followed = True
            return redirect(f'/profile/{session_user}')
 
    else:
        return redirect(f'/profile/{session_user}')
   



def search_user(request):
	
	if request.method == "POST":
		query = request.POST['query']

		if query:
			users = User.objects.filter(username__contains=query)

			if users:
				for user in users:
					messages.info(request, user.username)
					
			else:
				messages.error(request, "Username not found")
				
			return render(request=request, template_name="search_user.html")

		else:
			print("Please type username")
			return render(request=request, template_name="search_user.html")

	return render(request=request, template_name="search_user.html")
