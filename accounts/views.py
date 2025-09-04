from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Basic validation
        if password1 != password2:
            messages.error(request, "Passwords don't match.")
            return redirect('accounts:register')
        
        if len(password1) < 6:
            messages.error(request, "Password must be at least 6 characters.")
            return redirect('accounts:register')
        
        # Create user
        try:
            from django.contrib.auth.models import User
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            messages.success(request, f'Welcome {username}! Your account was created successfully.')
            return redirect('home')
        except:
            messages.error(request, "Username already exists. Please choose another.")
            return redirect('accounts:register')
    
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')