from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from user.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)

    def clean(self):
        super().clean()
        
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            
            if not user:
                raise forms.ValidationError("Invalid username or password")
            
            self.user = user
        return self.cleaned_data
