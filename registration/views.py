# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from .forms import *
from .models import *
from .tokens import account_activation_token
from django.utils.encoding import force_text,force_bytes
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = "index.html"

class LoginPageView(TemplateView):
    template_name = "login.html"



def login_view(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(email=email, password=password)
		if user is not None and user.is_active:
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			return redirect("home")
		return render(request, 'login.html', {'message':'UserName and Password is wrong' })
	return render(request, 'login.html', {'login_form': LoginForm,'signup_form':SignUpForm })

def logout_view(request):
    logout(request)
    return redirect("index")




def sign_up(request):
	current_site = get_current_site(request)
	if request.method == "POST":
		form = SignUpForm(data=request.POST)

		if form.is_valid():

			try:
				user=MyUser.objects.create_user(
					email=form.cleaned_data['email'],
					password=form.cleaned_data['password'],
					)
				user.is_active=False
				user.save()
				message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
 				send_mail("Email", message,'hitesh.mandhyan@gmail.com',
    [user.email], fail_silently=False)
				
				return render(request, 'login.html', {'message':'EMAIL has been sent to your registered account' })
			except:
				return render(request, 'login.html', {'message':'The Email Id has been used before' })
	else:
		return render(request, 'login.html', {'login_form': LoginForm,'signup_form':SignUpForm })


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
       
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
    else:
        return redirect('index')

@login_required
def CompanyInfoView(request):
	user=request.user
	if request.method == 'POST':
		form = CompanyInfoForm(request.POST, request.FILES)
		if form.is_valid():
			obj=form.save(commit=False)
			obj.company_account=user
			obj.save()
			return redirect('home')
		
	else:
		form = CompanyInfoForm()
	return render(request, 'details.html', {
        'form': form
    })

@login_required
def dashboard(request):
	user=request.user
	try:
		obj=CompanyInfo.objects.get(company_account=user)
		return HttpResponse("DASHBOARD")
	except:
		return redirect('companyinfo')
