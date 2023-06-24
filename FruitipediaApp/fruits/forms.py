from django import forms

from fruits.models import Fruit


class FruitCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ""

    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'image_url': 'Image URL'
        }


class FruitDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description']
        labels = {
            'image_url': 'Image URL',
        }
