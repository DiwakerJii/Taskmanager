from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from Taskman.models import TODO

class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title' , 'priority', 'status'  ]

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User 
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")



