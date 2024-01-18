from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm



class UserAppCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','image','whatsapp_number', 'email']




class LoginForm(forms.Form):
    email= forms.EmailField()
    password=forms.CharField(max_length=50, widget=forms.PasswordInput)


