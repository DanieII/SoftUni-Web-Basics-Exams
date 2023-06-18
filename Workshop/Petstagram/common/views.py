from django.shortcuts import render, redirect
from django.urls import reverse
from common.forms import CommentForm, SearchForm
from common.models import Like
from photos.models import Photo
from pyperclip import copy


def get_photo_url(request, photo_id):
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def home(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos,
        'search_form': SearchForm(),
        'comment_form': CommentForm(),
    }
    return render(request, 'common/home-page.html', context)


def search_by_pet_name(request):
    if request.method == 'GET':
        pet_name_query = request.GET['pet_name']
        photos = Photo.objects.all().filter(tagged_pets__name__icontains=pet_name_query)

        context = {
            'all_photos': photos,
            'search_form': SearchForm(),
            'comment_form': CommentForm(),
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


def comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
