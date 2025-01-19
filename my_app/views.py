from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import PhotoForm, SignUpForm
from .models import Photo, Tag
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    title = request.GET.get('title', None)  
    
    if title:
        photos = Photo.objects.filter(title__icontains=title)
    else:
        photos = Photo.objects.all()  

    return render(request, 'home.html', {'photos': photos})

@login_required  
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user  
            photo.save()
            return redirect('profile')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

@login_required  
def profile(request):
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'profile.html', {'photos': photos})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def like_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    photo.likes += 1
    photo.save()
    return redirect('home')

@login_required
def unlike_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if photo.likes > 0:
        photo.likes -= 1
    photo.save()
    return redirect('home')

@login_required
def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.user == photo.user:
        photo.delete()
    return redirect('profile')
