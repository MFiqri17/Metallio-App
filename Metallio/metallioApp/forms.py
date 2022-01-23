from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email', 'password1', 'password2']
        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control form-control-user",
                'placeholder': 'Email Address'
            })
        }

    def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget = TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Username'})        
            self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Password'})
            self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Repeat your password'})        
        
class ProfileRegisterForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['fullName', 'nickName']
        widgets = {
            'fullName': TextInput(attrs={
                'class': "form-control form-control-user",
                'placeholder': 'Full Name'
            }),
            'nickName': TextInput(attrs={
                'class': "form-control form-control-user",
                'placeholder': 'Nick Name'
            })
        }
        
        
class MetallioRegisterForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'    
        exclude = ['user', 'pembayaran']
        
class Pilihan1(ModelForm):
    class Meta:
        model = Pilihan1
        fields = ['pilihan']   


class Pilihan2(ModelForm):
    class Meta:
        model = Pilihan2
        fields = '__all__' 
        
        
        
class BendaharaForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        
        
                          
           
                
        