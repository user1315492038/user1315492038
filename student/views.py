from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

from . import models
from .forms import UserForm,RegisterForm

# Create your views here.
def index(request:HttpRequest):
    return HttpResponse(r"welcome!")

def login(request:HttpRequest):
    if request.session.get('is_login', None):  
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.student_info.objects.get(username=username)
                if user.password == password:  
                    request.session['is_login'] = True  
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index/')
            except:
                message = "User not exists"
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())

def register(request:HttpRequest):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid(): 
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            if password1 != password2: 
                message = "Different input!"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.student_info.objects.filter(username=username)
                if same_name_user:
                    message = 'User name already exists'
                    return render(request, 'register.html', locals())
                
                new_user = models.student_info.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.save()
                return redirect('/user/login/') 
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def logout(request:HttpRequest):
    if not request.session.get('is_login', None):  
        return redirect("/index/")
    request.session.flush()  
    return redirect('/index/')