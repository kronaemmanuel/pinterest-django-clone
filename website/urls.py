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
    path('saved_pins', views.SavedPins.as_view(), name='saved_pins'),
    path('<int:pin_id>/save_pin', views.save_pin, name='save_pin'),
    path('<int:pin_id>/unsave_pin', views.unsave_pin, name='unsave_pin'),
    path('<username>/upload', views.Upload.as_view(), name='upload')
]
