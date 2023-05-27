from django.shortcuts import render, redirect, get_object_or_404

from books.forms import BookForm
from books.models import Book
from users.models import Profile
from users.views import create_profile


def get_books_by_3(books):
    result = []
    current = []
    for i, book in enumerate(books, 1):
        if len(current) < 3:
            current.append(book)
            if i == len(books):
                result.append(current)
        else:
            result.append(current)
            current.clear()

    return result


def home(request):
    # For the exam there shouldn't be a login/register system and only one account needs to be created
    try:
        profile = Profile.objects.first()
    except:
        return create_profile(request)

    books = get_books_by_3(Book.objects.all())
    print(books)
    context = {
        'books': books,
        'profile': profile,
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = BookForm()

    context = {
        'form': form,
        'profile': Profile.objects.first()
    }
    return render(request, 'add-book.html', context)


def book_details(request, id):
    book = get_object_or_404(Book, id=id)

    context = {
        'book': book,
    }
    return render(request, 'book-details.html', context)


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)

    context = {
        'form': form,
    }
    return render(request, 'edit-book.html', context)


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('home')
