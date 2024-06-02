from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Renders the home page.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'home.html')

def about(request):
    """
    Renders the about page.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered about page.
    """
    return render(request, 'about.html')

def discography(request):
    """
    Renders the discography page.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered discography page.
    """
    return render(request, 'discography.html')

def tour(request):
    """
    Renders the tour page.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered tour page.
    """
    return render(request, 'tour.html')

def contact(request):
    """
    Renders the contact page.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered contact page.
    """
    return render(request, 'contact.html')

def signup(request):
    """
    Handles user signup.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered signup page or redirects to the login page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def user_profile(request):
    """
    Renders the user profile page.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered user profile page.
    """
    return render(request, 'user_profile.html')
