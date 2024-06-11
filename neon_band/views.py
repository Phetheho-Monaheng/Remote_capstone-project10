from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    """
    Render the home page of the Neon Band website.

    :param request: HttpRequest object
    :return: HttpResponse object representing the rendered home page
    """
    return render(request, 'neon_band/home.html')


@login_required
def about(request):
    """
    Render the about page providing information about the Neon Band.

    :param request: HttpRequest object
    :return: HttpResponse object representing the rendered about page
    """
    return render(request, 'neon_band/about.html')


@login_required
def discography(request):
    """
    Render the discography page displaying the music releases of the Neon Band.

    :param request: HttpRequest object
    :return: HttpResponse object representing the rendered discography page
    """
    return render(request, 'neon_band/discography.html')


@login_required
def tour(request):
    """
    Render the tour page showcasing the upcoming tour dates and locations of the Neon Band.

    :param request: HttpRequest object
    :return: HttpResponse object representing the rendered tour page
    """
    return render(request, 'neon_band/tour.html')


@login_required
def contact(request):
    """
    Render the contact page allowing users to get in touch with the Neon Band.

    :param request: HttpRequest object
    :return: HttpResponse object representing the rendered contact page
    """
    return render(request, 'neon_band/contact.html')


def signup(request):
    """
    Handle user signup process.

    If the request method is POST, validates the signup form data. If the form data is valid,
    creates a new user account and redirects the user to the login page. If the form data is
    invalid, re-renders the signup form with error messages.

    If the request method is GET, renders the signup form.

    :param request: HttpRequest object
    :return: HttpResponse object representing the rendered signup page or redirection to login page
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'neon_band/signup.html', {'form': form})


@login_required
def user_profile(request):
    """
    Render the user profile page for authenticated users.

    :param request: HttpRequest object
    :return: HttpResponse object representing the rendered user profile page
    """
    return render(request, 'neon_band/user_profile.html')
