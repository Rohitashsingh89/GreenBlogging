import re
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Last Name'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-user', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-user', 'placeholder': 'Email Address'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-user', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-user', 'placeholder': 'Repeat Password'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise forms.ValidationError("Username must not contain special characters.")
        
        # Check if the username is already in use
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already in use.")
        
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email already exist.")
        return email

class EmailAuthenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username') 
        password = self.cleaned_data.get('password')
        self.user_cache = authenticate(self.request, username=username, password=password)
        if self.user_cache is None:
            raise forms.ValidationError('Invalid email or password.')
        elif not self.user_cache.is_active:
            raise forms.ValidationError('This account is inactive.')
        return self.cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']

    