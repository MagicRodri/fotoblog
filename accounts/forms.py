from pyexpat import model
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username' : forms.TextInput(attrs={
                'class' : 'username_field',
            }),
            'password':forms.PasswordInput(attrs={
                'class' : 'password_field',
            })
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','role']

class PpUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['picture']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','role']

class FollowCreatorForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['follows']