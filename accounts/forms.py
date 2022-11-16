from .models import Profile
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username", widget=forms.TextInput)
    email_adress = forms.CharField(label="Email", widget=forms.EmailInput)
    first_name = forms.CharField(label="Input your first name", widget=forms.TextInput)
    last_name = forms.CharField(label="Input your last name", widget=forms.TextInput)
    password = forms.CharField(label="Paasword:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat your password:", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email_adress', 'first_name', 'last_name')

    def clean_password_validation(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords don't match!")
        return data['password']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'biography', 'photo')
