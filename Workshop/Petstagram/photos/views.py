from django.shortcuts import render

from photos.models import Photo


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.count()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }
    return render(request, 'photos/photo-details-page.html', context)
