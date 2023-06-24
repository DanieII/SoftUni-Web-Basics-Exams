from django import forms

from profiles.models import Profile


class ProfileCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ""

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.TextInput(attrs={'placeholder': 'Password', 'type': 'password'})
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image_url', 'age']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
            'age': 'Age'
        }
