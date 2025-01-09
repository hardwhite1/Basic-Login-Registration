from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("Register")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("Register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("Register")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, "User created successfully.")
        return redirect("login")
    return render(request, "Register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in ")
            return redirect("test")
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect("login")
    return render(request, "Login.html")
