from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import redirect, render
from django import forms


def index(request):
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
        return redirect('website:index')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request=request, username=username, password=password)

            if user.is_authenticated:
                auth.login(request, user)
                return redirect('website:index')

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


def profile(request):
    return render(request, 'website/profile.html')


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


def profile_update(request):
    if not request.user.is_authenticated:
        return redirect('website:login')

    if request.method == 'POST':
        form = UserUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'User updated successfully')
            return redirect('website:profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'website/user_update_form.html', {'form': form})


def feed(request):
    if not request.user.is_authenticated:
        return redirect('website:login')

    return render(request, 'website/feed.html')


def saved_pins(request):
    if not request.user.is_authenticated:
        return redirect('website:login')

    return render(request, 'website/saved_pins.html')
