from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *


class UserLoginForm(AuthenticationForm):
    phone_number = forms.CharField(label='phone_number',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=('phone_numbenr','password')

class UserRegisterForm(UserCreationForm):
    username=forms.CharField(max_length=150,label='username',
    widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 =forms.CharField(max_length=150,label='password1',
    widget=forms.TextInput(attrs={"class":"form-control"}))
    password2 =forms.CharField(max_length=150,label='password2',
    widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(label='E-mail',widget=forms.EmailInput(attrs={'class':'form-control'}))

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('full_name', 'phone', 'location', 'teacher')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
        }
class SubjectsForm(forms.ModelForm):
    class Meta:
        model=Teacher
        #fields='__all__'
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }
