from django.shortcuts import render, redirect
from django.urls import reverse

from common.models import Like
from photos.models import Photo
from pyperclip import copy


def get_photo_url(request, photo_id):
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def home(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos
    }
    return render(request, 'common/home-page.html', context)


def like(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    # TODO: Check whether whoever is liking has liked before
    like_to_photo = Like.objects.filter(to_photo=photo).first()

    if like_to_photo:
        like_to_photo.delete()
    else:
        Like.objects.create(to_photo=photo)

    return get_photo_url(request, photo_id)


def share(request, photo_id):
    copy(request.META['HTTP_HOST'] + reverse('photo details', kwargs={'pk': photo_id}))

    return get_photo_url(request, photo_id)
