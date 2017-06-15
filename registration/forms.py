from django import forms
from .models import CompanyInfo 



class LoginForm(forms.Form):
    email = forms.CharField(label="email", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class SignUpForm(forms.Form):
    email = forms.CharField(label="email", max_length=30,
                               widget=forms.TextInput(attrs={ 'name': 'email'}))
    password = forms.CharField(label="password", max_length=30,
                               widget=forms.PasswordInput(attrs={ 'name': 'password'}))
    password2 = forms.CharField(label="password2",max_length=100,
                                widget=forms.PasswordInput(attrs={ 'name': 'password2'}))

class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        exclude = ['company_account']

    
