from django.shortcuts import render, redirect
from account.forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            message = form.cleaned_data['username'].title() + ' ,вы успешно зарегистрированы!'
            messages.success(request, message)
            return redirect('login')
        else:
            messages.error(request, 'Проверьте введённые данные')
    else:
        if request.user.is_active:
            return redirect('login')
        form = UserRegisterForm()
    context = {'title': 'Регистрация', 'form': form}
    return render(request, 'account/register.html', context)


def user_login(request):
    """Проверяем метод запроса, поля"""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно зашли на сайт')
            return redirect('home')
        else:
            messages.error(request, 'Неверный логин или пароль')
    else:
        form = UserLoginForm()
    context = {'title': 'Логин', 'form': form}
    return render(request, 'account/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')