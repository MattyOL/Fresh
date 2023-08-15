from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

class CustomSignupForm(UserCreationForm):
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
            return redirect('signup2')
        return password

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']