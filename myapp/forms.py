from django import forms
from myapp.models import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields =('username','first_name','last_name','email','password',)
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

        
    
        
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class: ': 'form-control'}))

    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class: ': 'form-control'}))


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields="__all__"
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields=('review','rating')
        widgets={
            'review': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control','min':0.0,'max':10.0}),}