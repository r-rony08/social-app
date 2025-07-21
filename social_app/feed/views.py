from django.shortcuts import render, HttpResponseRedirect

from users.forms import CreateNewUser, EditProfile
from users.models import UserProfile

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def feed(request):
    return render(request, 'feed/home_feed.html', context={'title':'Home Feed'})