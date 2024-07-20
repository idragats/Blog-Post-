from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import RegisterForm

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('home') 
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    error_message = None
    registration_url = reverse('register')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                next_url = request.POST.get('next') or request.GET.get('next') or 'home'
                return redirect(next_url)
            else:
                error_message = "Authentication failed. User is None."
        else:
            error_message = f"Invalid Credentials. Don't you have an account? <a href='{registration_url}'>Sign up here</a>"
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form, 'error': error_message})
    
    
@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')  # Redirect to the homepage after logout
    return render(request, 'registration/logout.html') 
