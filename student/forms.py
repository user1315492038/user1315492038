from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="account", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", max_length=18, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    name = forms.CharField(label="account", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="password", max_length=18, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="repeat password", max_length=18, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    sex = forms.CharField(label="sex", max_length=7, widget=forms.TextInput(attrs={'class': 'form-control'}))
    citizen_id = forms.CharField(label="citizen id", max_length=18, widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_id = forms.CharField(label="student_id", max_length=19, widget=forms.TextInput(attrs={'class': 'form-control'}))
    school = forms.CharField(label="school", max_length=7, widget=forms.TextInput(attrs={'class': 'form-control'}))
    in_class = forms.CharField(label="class", max_length=7, widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.CharField(label="status", max_length=7, widget=forms.TextInput(attrs={'class': 'form-control'}))