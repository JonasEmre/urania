from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-group__input'})

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-group__input'})

