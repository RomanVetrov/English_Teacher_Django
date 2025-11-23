from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "email": "Email",
        }

    # здесь можем добавить любую валидацию
    def clean_first_name(self):
        name = self.cleaned_data["first_name"].strip()
        if len(name) < 2:
            raise forms.ValidationError("Слишком короткое имя")
        return name

    def clean_last_name(self):
        name = self.cleaned_data["last_name"].strip()
        if len(name) < 2:
            raise forms.ValidationError("Слишком короткая фамилия")
        return name
    


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            self.user = authenticate(
                request=self.request,   # ← ВАЖНО
                email=email,
                password=password
            )

            if self.user is None:
                raise ValidationError("Неверный email или пароль")

        return cleaned_data

    def get_user(self):
        return self.user
