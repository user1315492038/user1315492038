from django.shortcuts import render,redirect
from django.http import HttpRequest

from . import models
from .forms import UserForm,RegisterForm

# Create your views here.
def index(request:HttpRequest):
    return render(request,'index.html')

def details(request:HttpRequest):
    if not request.session.get('is_login', None):
        return render(request,'index.html')
    else:
        return render(request,'details.html')

def login(request:HttpRequest):
    if request.session.get('is_login', None):  
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.student_info.objects.get(name=username)
                if user.password == password:  
                    request.session['is_login'] = True  
                    request.session['user_name'] = user.name
                    request.session['sex'] = user.sex
                    request.session['citizen_id'] = user.citizen_id
                    request.session['student_id'] = user.student_id
                    request.session['school'] = user.school
                    request.session['class'] = user.in_class
                    request.session['status'] = user.status
                    request.session['password'] = user.password
                    return redirect('/index/')
            except:
                message = "User not exists"
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())

def logout(request:HttpRequest):
    if not request.session.get('is_login', None):  
        return redirect("/index/")
    
    request.session.flush()  
    return redirect('/index/')

"""
def register(request:HttpRequest):
    if request.session.get('is_login', None):
        return redirect("/index/")
    
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid(): 
            studentname = register_form.cleaned_data['name']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            sex = register_form.cleaned_data['sex']
            citizen_id = register_form.cleaned_data['citizen_id']
            student_id = register_form.cleaned_data['student_id']
            school = register_form.cleaned_data['school']
            in_class = register_form.cleaned_data['in_class']
            status = register_form.cleaned_data['status']

            message = "unused"

            if password1 != password2: 
                message = "Different input!"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.student_info.objects.filter(name=studentname)
                if same_name_user:
                    message = 'User name already exists'
                    return render(request, 'register.html', locals())
            if message != "unused":
                return redirect('/index/')
            else:
                new_user = models.student_info.objects.create()
                new_user.name = studentname
                new_user.password = password1
                new_user.sex = sex
                new_user.citizen_id = citizen_id
                new_user.student_id = student_id
                new_user.school = school
                new_user.in_class = in_class
                new_user.status = status
                new_user.save()
                return redirect('/login/')
    register_form = RegisterForm()
    return render(request, 'register.html', locals())
"""
def register(request: HttpRequest):
    if request.session.get('is_login', None):
        return redirect("/index/")
    
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid(): 
            studentname = register_form.cleaned_data['name']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            sex = register_form.cleaned_data['sex']
            citizen_id = register_form.cleaned_data['citizen_id']
            student_id = register_form.cleaned_data['student_id']
            school = register_form.cleaned_data['school']
            in_class = register_form.cleaned_data['in_class']
            status = register_form.cleaned_data['status']

            if password1 != password2: 
                message = "Different input!"
                return render(request, 'register.html', locals())
            
            same_name_user = models.student_info.objects.filter(name=studentname)
            if same_name_user:
                message = 'User name already exists'
                return render(request, 'register.html', locals())
            
            # If all checks pass, create the new user
            new_user = models.student_info(
                name=studentname,
                password=password1,
                sex=sex,
                citizen_id=citizen_id,
                student_id=student_id,
                school=school,
                in_class=in_class,
                status=status
            )
            new_user.save()
            return redirect('/login/')
    
    register_form = RegisterForm()
    return render(request, 'register.html', locals())