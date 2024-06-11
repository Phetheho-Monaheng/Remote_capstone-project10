from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# View for rendering the login page
def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            auth_login(request, user)
            # Redirect to the home page after successful login
            return redirect('neon_band:home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# View for rendering the logout page
def my_logout(request):
    return render(request, 'accounts/logout.html')

# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Authenticate and log in the user
            return redirect('neon_band:home')  # Redirect to home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registration.html', {'form': form})

@login_required
def home(request):
    # Your home view logic here
    return render(request, 'home.html')