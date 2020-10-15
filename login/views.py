from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout, get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required


def welcome(request):
    if request.user.is_authenticated:
        return render(request, "users/apps.html")
    return redirect('/login')


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


@login_required(login_url='login')
def register(request):
    form = MyUserCreationForm
    if request.method == "POST":
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('apps')

    return render(request, "users/register.html", {'form': form})


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                fav_color = request.session.get('fav_color', 'red')
                return redirect('apps')
    return render(request, "users/login.html", {'form': form})


def logout(request):
    do_logout(request)
    return redirect('/')

