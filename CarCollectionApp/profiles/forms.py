from django import forms

from profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
