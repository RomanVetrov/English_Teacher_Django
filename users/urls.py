from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


class PostOnlyLogoutView(LogoutView):
    http_method_names = ["post", "head", "options"]  # только POST (и служебные HEAD/OPTIONS)


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", PostOnlyLogoutView.as_view(next_page="home"), name="logout"),
]
