from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RatingForm(forms.Form):
    rating = forms.IntegerField(label='Rating')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('favorite_movie', 'ratings')
