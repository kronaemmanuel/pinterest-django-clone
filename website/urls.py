from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('<username>/profile', views.profile, name='profile'),
    path('<username>/profile_update', views.ProfileUpdate.as_view(), name='profile_update'),
    path('feed', views.Feed.as_view(), name='feed'),
    path('saved_pins', views.saved_pins, name='saved_pins'),
    path('upload', views.upload, name='upload')
]
