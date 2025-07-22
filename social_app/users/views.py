from django.shortcuts import render, HttpResponseRedirect
from users.forms import CreateNewUser, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from users.models import UserProfile,Follow
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from feed import views
from feed.forms import PostForm
from feed.models import Post

# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    register = False
    if request.method == "POST":
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            register = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('users:login'))
        
    return render(request, 'users/signup.html', context={'title':'SignUp Form Here', 'form':form })



def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('feed:feed'))
            
    return render(request, 'users/login.html', context={'title':'Login Page Here', 'form':form })


@login_required
def edit_profile(request):
    current_user, created = UserProfile.objects.get_or_create(user=request.user)
    form = EditProfile(instance=current_user)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('users:profile'))

    return render(request, 'users/profile.html', context={'title':'Profile Page Here', 'form':form })


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


@login_required
def profile(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('feed'))
    user_posts = Post.objects.filter(author=request.user)

    return render(request, 'users/user.html', context={'title': "User Profile", 'form':form, 'user_posts': user_posts})