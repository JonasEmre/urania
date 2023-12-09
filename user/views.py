from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from notes.models import Note
from notes.forms import CreateNoteForm


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You are not logged in!')
        return redirect('login')

    notes = Note.objects.filter(user_id=request.user)

    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            Note.objects.create(
                title=title, content=content, user_id=request.user)
            messages.success(request, 'You created a note.')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid note')
    else:
        form = CreateNoteForm()

    return render(request, 'user/profile.html', {'notes': notes, 'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, f'Welcome {user.username}')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f'We will miss you {request.user.username}')
        logout(request)
        return redirect('home')
    else:
        messages.warning(request, 'You are not logged in!')
        return redirect('login')
