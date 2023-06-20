from django import forms

from plants.models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class DeletePlantForm(PlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
