from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    fullname = models.CharField(max_length=264, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)
    # phone_number = models.CharField(max_length=20, blank=True)
    # gender = models.CharField(max_length=10, blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    # location = models.CharField(max_length=100, blank=True)
    # privacy = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')], default='public')
    # is_verified = models.BooleanField(default=False)


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')