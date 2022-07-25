from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import redirect, render


def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('website:index')
        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'website/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'website/logout.html')


def index(request):
    if not request.user.is_authenticated:
        return redirect('website:login')

    return render(request, 'website/index.html')


def register(request):
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


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


def user_update(request):
    if not request.user.is_authenticated:
        return redirect('website:login')

    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'User updated successfully')
            return redirect('website:index')
    else:
        form = UserForm(instance=request.user)

    return render(request, 'website/user_update_form.html', {'form': form})
