# user/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telephone_number = forms.CharField(max_length=15)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'telephone_number', 'avatar', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_telephone_number(self):
        telephone_number = self.cleaned_data.get('telephone_number')
        if CustomUser.objects.filter(telephone_number=telephone_number).exists():
            raise forms.ValidationError("This telephone number is already in use.")
        return telephone_number

class CustomUserUpdateForm(UserChangeForm):
    password = None  # Remove password field from update form

    email = forms.EmailField(required=True)
    telephone_number = forms.CharField(max_length=15)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'telephone_number', 'avatar', 'username')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.instance and CustomUser.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_telephone_number(self):
        telephone_number = self.cleaned_data.get('telephone_number')
        if self.instance and CustomUser.objects.exclude(pk=self.instance.pk).filter(telephone_number=telephone_number).exists():
            raise forms.ValidationError("This telephone number is already in use.")
        return telephone_number
