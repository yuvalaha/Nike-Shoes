from django.db import models
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django import forms

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]      
        widgets = {
            "first_name": TextInput(attrs={"class":"form-control", "minlength": 2, "maxlength": 30}),
            "last_name": TextInput(attrs={"class":"form-control", "minlength": 2, "maxlength": 30}),
            "email": EmailInput(attrs={"class":"form-control", "maxlength":100}),
            "password": PasswordInput(attrs={"class":"form-control", "minlength": 4, "maxlength": 20})
        }
        
    
    def save(self):
        
        # Create user without saving in the database.
        user = super().save(commit=False)
        
        # Enter email into user name
        user.username = self.cleaned_data["email"]
        
        # Get existing user
        existing_user = User.objects.filter(email=user.email).first()

        if existing_user:
        # Handle the situation where the email is already in use
            raise forms.ValidationError("This email address is already registered.")
        
        # Hash password 
        user.password = make_password(self.cleaned_data["password"])
        
        # Save user in the database
        user.save()
        
        # Return User
        return user
    
    
    
    # ------------------------------------------------------------------------------------------
    
class LoginForm(ModelForm):
        
    class Meta:
        model = User
        fields = ["email", "password"]      
        widgets = {
            "email": EmailInput(attrs={"class":"form-control", "maxlength":100}),
            "password": PasswordInput(attrs={"class":"form-control", "minlength": 4, "maxlength": 20})
        }
        