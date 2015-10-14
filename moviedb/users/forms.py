from django import forms
from django.contrib.auth.models import User
from .models import Profile
from database.models import Rating

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('favorite_movie', 'ratings')


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars', 'text']
