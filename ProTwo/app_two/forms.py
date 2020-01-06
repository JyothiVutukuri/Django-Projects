from django import forms
from django.contrib.auth.models import User
from app_two.models import MyUser, Profile


class FormOne(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = '__all__'


class ProfileInForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ProfileExtendForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('profile_site', 'profile_photo')

