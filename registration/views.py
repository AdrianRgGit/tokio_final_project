from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "registration/login.html")


def signup(request):
    return render(request, "registration/signup.html")


@login_required
def profile(request):
    return render(request, "registration/profile.html")
