from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import UserProfile


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Email or Mobile Number'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))




    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EditProfile(forms.ModelForm):

    birth_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date', }))

    class Meta:
        model = UserProfile
        exclude = ('user',)