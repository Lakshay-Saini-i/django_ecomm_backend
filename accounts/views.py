from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import Profile

# Create your views here.


def login_page(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)
        
        if not user_obj.exists():
            messages.warning(request, 'Please register to continue')
            return HttpResponseRedirect(request.path_info)
        
        print(f' user_obj = {user_obj[0]}')
        if user_obj[0].profile.is_email_verified:
            messages.warning(request, 'your account is not verified')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(request, username = email,  password = password)
        if user_obj:
            login(request, user_obj)
            print('logged in')
            return render(request, 'base/base.html')
        messages.warning(request, 'Wrong username or password')

    return render(request, 'accounts/login.html')

def register_page(request):
    print('register method called 1')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=email)

        if user_obj.exists():
            messages.warning(request, 'Username already exists')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(first_name = first_name, last_name = last_name, email = email, username = email)
        print(f'**** password is {password}')
        user_obj.set_password(password)
        user_obj.save()
        print('register method called 2')
        messages.success(request, 'Email has been sent to the register email address')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/register.html')

def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token = email_token)
        user.is_email_verified = True
        user.save()
    except Exception as e:
        return HttpResponse('Invalid Request')
    return redirect('/')


    