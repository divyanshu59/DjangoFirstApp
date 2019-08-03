from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}!')
            return redirect('home')

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
def login(request):
    return render(request, 'login.html', {})