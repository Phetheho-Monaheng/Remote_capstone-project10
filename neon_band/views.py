from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    """
    Renders the home page.

    :param request: The request object.
    :type request: HttpRequest
    :return: The rendered home page.
    :rtype: HttpResponse
    """
    return render(request, 'home.html')

def about(request: HttpRequest) -> HttpResponse:
    """
    Renders the about page.

    :param request: The request object.
    :type request: HttpRequest
    :return: The rendered about page.
    :rtype: HttpResponse
    """
    return render(request, 'about.html')

def discography(request: HttpRequest) -> HttpResponse:
    """
    Renders the discography page.

    :param request: The request object.
    :type request: HttpRequest
    :return: The rendered discography page.
    :rtype: HttpResponse
    """
    return render(request, 'discography.html')

def tour(request: HttpRequest) -> HttpResponse:
    """
    Renders the tour page.

    :param request: The request object.
    :type request: HttpRequest
    :return: The rendered tour page.
    :rtype: HttpResponse
    """
    return render(request, 'tour.html')

def contact(request: HttpRequest) -> HttpResponse:
    """
    Renders the contact page.

    :param request: The request object.
    :type request: HttpRequest
    :return: The rendered contact page.
    :rtype: HttpResponse
    """
    return render(request, 'contact.html')

def signup(request: HttpRequest) -> HttpResponse:
    """
    Handles user signup.

    :param request: The request object.
    :type request: HttpRequest
    :return: The rendered signup page or redirects to the login page.
    :rtype: HttpResponse
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
def user_profile(request: HttpRequest) -> HttpResponse:
    """
    Renders the user profile page.

    :param request: The request object.
    :type request: HttpRequest
    :return: The rendered user profile page.
    :rtype: HttpResponse
    """
    return render(request, 'user_profile.html')
