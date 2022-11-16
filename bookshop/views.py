from django.shortcuts import render
from .models import Author, Book
from cart.cart import Cart



def index(request):
    visits = request.session.get('visits', 0)
    request.session['visits'] = visits + 1

    cart = Cart(request)
    books_amount = Book.objects.count()
    author_amount = Author.objects.count()
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books,
                                          'visits': visits, 
                                          'books_amount': books_amount,
                                          'author_amount': author_amount,
                                          'cart': cart})


def book(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'view.html', {'book': book})

def buy(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'buy.html', {'book': book})
