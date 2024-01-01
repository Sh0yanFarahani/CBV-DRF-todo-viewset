from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    password1 = forms.CharField(max_length=200)
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')        

    def save(self):   
        password1 = self.cleaned_data['password1']
        email = self.cleaned_data['email']
        user = CustomUser.objects.create_user(email=email, password=password1, is_verified=False, is_active=True)

        return user