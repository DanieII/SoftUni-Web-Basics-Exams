from django import forms

from cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class DeleteCarForm(CarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for line in self.fields.values():
            line.disabled = True
