from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

# Custom validator function to ensure username only contains letters and numbers
def validate_username_only_letters_digits(value):
    if not re.match(r'^[a-zA-Z0-9]+$', value):
        raise ValidationError("Username can only contain letters and digits. No special characters allowed.")
    
# Custom signup form that extends Django's UserCreationForm
class SignupForm(UserCreationForm):
    # Add email field (not included in default UserCreationForm)
    email = forms.EmailField(required=True)
    
    # Override username field to add custom validator
    username = forms.CharField(
        max_length=150,
        required=True,
        validators=[validate_username_only_letters_digits],
    )

    # Meta class to specify model and form fields
    class Meta:
        model = User  # Use Django's built-in User model
        fields = ['username', 'email', 'password1', 'password2']  # Fields to include in the form

    # Custom validation method for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Check if username already exists (case-insensitive)
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    # Custom validation method for email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if email already exists (case-insensitive)
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    
# View function to handle user signup
def signup(request):
    if request.method == 'POST':  
        # If form is submitted
        form = SignupForm(request.POST)  # Create form instance with submitted data
        if form.is_valid():  # Check if form data is valid
            # Save the new user
            user = form.save()
            # Automatically log in the new user
            login(request, user)
            # Add success message
            messages.success(request, "You've signed up successfully and are now logged in. Welcome to Eato!")
            # Redirect to home page
            return redirect('index')
    else:  
        # If GET request, show empty form
        form = SignupForm()

    # Render signup template with form
    return render(request, 'registration/signup.html', {'form': form})
