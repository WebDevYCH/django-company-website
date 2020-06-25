
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# 登录表单
class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={"class": "input100"})
        self.fields['password'].widget = widgets.PasswordInput(attrs={"class": "input100"})

    
class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = widgets.TextInput(attrs={"class": "input100"})
        self.fields['email'].widget = widgets.EmailInput(attrs={"class": "input100"})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={"class": "input100"})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={"class": "input100"})
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            raise ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError('Email already exists')
        return email

    

    class Meta:
        model = get_user_model()
        fields = ("username", "email")
