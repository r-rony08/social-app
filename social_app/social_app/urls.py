
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import  static
from feed import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',  include('users.urls') ),
    path('feed/',  include('feed.urls') ),
    path("", views.feed, name='feed'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
