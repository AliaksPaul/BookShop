from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})


def book(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'view.html', {'book': book})

def buy(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'buy.html', {'book': book})
