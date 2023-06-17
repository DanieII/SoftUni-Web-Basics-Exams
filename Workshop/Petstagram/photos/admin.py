from django.contrib import admin

from photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_of_publication', 'description', 'tagged_pets_names']

    @staticmethod
    def tagged_pets_names(photo_object):
        tagged_pets = photo_object.tagged_pets.all()
        if tagged_pets:
            return ', '.join([pet.name for pet in tagged_pets])
        return 'No tagged pets'
