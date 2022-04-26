from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from meal_tracker.auth_user.models import AuthUser, Profile

UserModel = get_user_model()

class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                },
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'
                }
            ),
        }

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        return self.cleaned_data['last_name']


    def save(self, commit=True):
        user = UserModel(
            email=self.cleaned_data['email'],
        )
        user.set_password(self.cleaned_data['password1'])
        user.save()
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )
        profile.save()
        return user


class ChangePasswordForm(auth_forms.PasswordChangeForm):

    class Meta:
        model = UserModel
        fields = '__all__'
