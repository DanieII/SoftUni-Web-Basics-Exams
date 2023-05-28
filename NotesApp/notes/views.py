from django.shortcuts import render, redirect, get_object_or_404

from notes.forms import NoteForm, DeleteNoteForm
from notes.models import Note
from users.models import Profile
from users.views import create_profile


def home(request):
    profile = Profile.objects.first()
    if not profile:
        return create_profile(request)

    notes = Note.objects.all()
    return render(request, 'home/home-with-profile.html', {'notes': notes})


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()

    return render(request, 'notes/note-create.html', {'form': form})


def edit_note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note-edit.html', {'form': form})


def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            note.delete()
            return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)

    return render(request, 'notes/note-delete.html', {'form': form})


def details_note(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, 'notes/note-details.html', {'note': note})
