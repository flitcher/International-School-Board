from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name', 'username', 'email', 'password1', 'password2']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['description','text']