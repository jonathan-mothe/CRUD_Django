from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm


def list_author(request):
    author = Author.objects.all()
    return render(request, 'index.html', {'author': author})


def create_author(request):
    form = AuthorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_author')

    return render(request, 'author-form.html', {'form': form})


def update_author(request, id):
    author = Author().objects.get(id=id)
    form = AuthorForm(request.POST or None, instance=author)

    if form.is_valid():
        form.save()
        return redirect('list_author')

    return render(request, 'author-form.html', {'form': form, 'author': author})


def delete_author(request, id):
    author = Author.objects.get(id=id)

    if request.method == 'POST':
        author.delete()
        return redirect('list_author')

    return render(request, 'author-delete-confirm.html', {'author': author})


def list_books(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})


def create_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_books')

    return render(request, 'books-form.html', {'form': form})


def update_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('list_books')

    return render(request, 'books-form.html', {'form': form, 'book': book})


def delete_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('list_books')

    return render(request, 'book-delete-confirm.html', {'book': book})



