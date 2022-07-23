from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


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
