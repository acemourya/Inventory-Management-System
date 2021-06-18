from .forms import NewUserForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def index(request):
    """index"""

    return redirect("./login")


def register_request(request):
    """Regitation or signup account employee"""

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful.")
            return redirect("../login")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request, "employees/register.html", {"register_form": form})


def login_request(request, *args, **kwargs):
    """Login account employee"""

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("../../products")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "employees/login.html", context)


def logout_request(request):
    """Logout account employee"""

    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("../../")
