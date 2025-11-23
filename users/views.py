from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .forms import LoginForm


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "Вы уже авторизованы.")
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request.POST, request=request)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, "Вы успешно вошли!")

            next_url = request.GET.get("next")
            if next_url:
                return redirect(next_url)

            return redirect("home")
    else:
        form = LoginForm(request=request)

    return render(request, "users/login.html", {"form": form})



def logout_view(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта.")
    return redirect("home")

