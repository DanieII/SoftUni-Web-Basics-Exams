from django import forms

from photos.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class EditPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']
