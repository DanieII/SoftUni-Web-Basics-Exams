from django import forms

from profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
