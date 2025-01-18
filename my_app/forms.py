from django import forms
from .models import Photo, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PhotoForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,  
        required=False
    )

    class Meta:
        model = Photo
        fields = ['title', 'description', 'image', 'tags']  

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
