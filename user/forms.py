from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter username', 'class': 'form-control'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter email', 'class': 'form-control'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter password', 'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm password', 'class': 'form-control'
        })

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Enter username', 'class': 'form-control'})
    )
    password = forms.CharField(max_length=150,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'form-control'})
    )

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

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'first_name', 'last_name', 'email', 'bio']
    
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com'
            }),
            'bio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about yourself...',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add HTML5 validation attributes
        self.fields['avatar'].widget.attrs.update({
            'accept': 'image/*',
            'class': 'form-control auth-file-input',
        })
        self.fields['username'].widget.attrs.update({
            'pattern': '[a-zA-Z0-9_]+',
            'title': 'Only letters, numbers and underscores are allowed',
            'class': 'form-control',
            'placeholder': 'Enter your username',
        })

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        
        if avatar:
            # File size validation (2MB max)
            max_size = 2 * 1024 * 1024  # 2MB
            if avatar.size > max_size:
                raise ValidationError("Image file too large (max 2MB)")
            
            # File extension validation
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
            ext = avatar.name.split('.')[-1].lower()
            if ext not in valid_extensions:
                raise ValidationError(f"Unsupported file extension. Allowed: {', '.join(valid_extensions)}")
            
            # Dimensions validation
            from PIL import Image
            try:
                img = Image.open(avatar)
                if img.width > 2000 or img.height > 2000:
                    raise ValidationError("Image dimensions too large (max 2000x2000px)")
            except:
                raise ValidationError("Invalid image file")
        
        return avatar

    def clean_username(self):
        username = self.cleaned_data['username']
        
        # Check if username changed
        if username == self.instance.username:
            return username
            
        # Username format validation
        if not username.isalnum() and '_' not in username:
            raise ValidationError("Username can only contain letters, numbers and underscores")
            
        # Username uniqueness
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("This username is already taken")
            
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        
        # Check if email changed
        if email == self.instance.email:
            return email
            
        # Email format validation
        if '@' not in email:
            raise ValidationError("Enter a valid email address")
            
        # Email uniqueness
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("This email is already registered")
            
        return email
