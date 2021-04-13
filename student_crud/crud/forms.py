from django import forms
from . models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "password"]
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),

        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']