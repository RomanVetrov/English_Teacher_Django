from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


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
