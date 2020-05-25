from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth.models import User
from .form import LoginForm, RegForm


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from',reverse('mysite:home')))  
    else:
        login_form = LoginForm()
    context = {}
    context['login_form'] = login_form
    return render(request, 'login/login.html', context)


def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password']
            email = reg_form.cleaned_data['email']

            # 注册用户
            user = User()
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()

            user = auth.authenticate(username=username,password=password)
            auth.login(request, user)

            return redirect(request.GET.get('from',reverse('mysite:home')))  

    else:
        reg_form = RegForm()
    context = {}
    context['reg_form'] = reg_form
    return render(request, 'login/register.html', context)

