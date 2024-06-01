from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="account", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", max_length=18, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="account", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="password", max_length=18, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="repeat password", max_length=18, widget=forms.PasswordInput(attrs={'class': 'form-control'}))