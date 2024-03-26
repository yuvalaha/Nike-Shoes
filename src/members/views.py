from django.shortcuts import render, redirect
from .models import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout 

# Register view
def register(request):
    # Get
    if request.method == "GET":
        context = {"active": "register", "form": RegistrationForm()}
        return render(request, "register.html", context)
    
    # Post
    form = RegistrationForm(request.POST)
    
    # Validation
    if not form.is_valid():
        context = {"active": "register", "form": form}
        return render(request, "register.html", context)
    
    # Saving the user in the database
    user = form.save()
    
    # Sending a success message 
    messages.success(request, "Welcome " + user.first_name + "!")
    
    # Save user in server-side session
    login(request, user)
    
    # Redirect
    return redirect("home")



# Login view
def log_in(request):
    
    # Get
    if request.method == "GET":
        context = {"active": "login", "form": LoginForm()}
        return render(request, "login.html", context)
    
    # Post
    
    form = LoginForm(request.POST)
    # Validation
    if not form.is_valid():
        context = {"active": "login", "form": LoginForm()}
        return render(request, "login.html", context)
        
    # Check if user name and password exists in the database 
    # Return user if exists or None if not exists
    user = authenticate(request, username = form.cleaned_data["email"], password = form.cleaned_data["password"])
    
    # User doesn't exist
    if not user:
        messages.error(request, "Incorrect email or password.")
        context = {"active": "login", "form": LoginForm()}
        return render(request, "login.html", context)
    
    # User exist
    login(request, user)
    messages.success(request, "Welcome back " + user.first_name + " " + user.last_name + "!")
    return redirect("home")

# Logout view
def log_out(request):
    messages.success(request, "Bye Bye")
    logout(request) # Remove the user from the server side session
    return redirect("home")