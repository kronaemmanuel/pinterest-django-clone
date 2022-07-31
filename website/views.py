from django import forms
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic.list import ListView

from .models import Pin, Profile


def index(request):
    if request.user.is_authenticated:
        return redirect('website:feed')

    return render(request, 'website/index.html')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


def login(request):
    if request.user.is_authenticated:
        return redirect('website:feed')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(
                request=request, username=username, password=password)

            if user.is_authenticated:
                auth.login(request, user)
                return redirect('website:feed')

    else:
        form = UserLoginForm()

    return render(request, 'website/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return render(request, 'website/logout.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('website:index')

    # Handle POST request as signup form submission
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('website:register')

    # Handle GET request as signup form page request
    else:
        form = UserCreationForm()

    return render(request, 'website/register.html', {'form': form})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'website/profile.html', {'user': user})


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdate(LoginRequiredMixin, View):
    template_name = 'website/user_update_form.html'

    def get(self, request, username):
        if not request.user.username == username:
            raise PermissionDenied

        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, username):
        if not request.user.username == username:
            raise PermissionDenied

        form = UserUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'User updated successfully')
            return redirect('website:profile', username=request.user.username)

        return render(request, self.template_name, {'form': form})


class Feed(LoginRequiredMixin, ListView):
    login_url = 'website:login'
    model = Pin
    context_object_name = 'pins'
    template_name = 'website/feed.html'

    def get_queryset(self):
        """
        Returns the pins ordered in reverse chronological order
        """
        return Pin.objects.order_by('-created_at')


@login_required
def saved_pins(request):
    return render(request, 'website/saved_pins.html')


class PinUploadForm(ModelForm):
    class Meta:
        model = Pin
        fields =  ['title', 'description', 'picture']


@login_required
def upload(request):
    if request.method == 'POST':
        form = PinUploadForm(request.POST, request.FILES)

        if form.is_valid():
            pin = form.save(commit=False)
            pin.user_profile = Profile.objects.get(user=request.user)
            pin.save()
            return redirect('website:feed')
        else:
            messages.error(request, 'There was a problem with your form, Please try again')
            return redirect('website:upload')

    else:
        form = PinUploadForm()
    return render(request, 'website/upload.html', {'form': form})
