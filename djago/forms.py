from django import forms
from .models import Projet

class ConnectForm(forms.Form):
    login = forms.CharField(max_length=30)
    m_pass = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class CreerProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        exclude = ("user", "donateurs", "Investisseurs")


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class InscriptionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")