from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django.contrib.auth import authenticate

class RegisterationForm(UserCreationForm):
    email = forms.EmailField(max_length=60,help_text='Add valid email')

    class Meta:
        model = Account
        fields =('email','username','firstname','lastname','password1','password2')

class AccountAuthenticationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email','password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email,password=password):
            raise forms.ValidationError('Invalid login')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model =  Account
        fields = ['firstname','lastname','username']
