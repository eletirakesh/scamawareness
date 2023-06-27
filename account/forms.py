
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
