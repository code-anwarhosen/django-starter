from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.forms import UserRegistrationForm, UserLoginForm


@login_required
def user_profile(request):
    return render(request, 'user/profile.html')


@login_required
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logout Successful!')
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            login(request, form.user)
            messages.success(request, 'Login Successful!')
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created account!')
            messages.success(request, 'You can login now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})
