from django.shortcuts import redirect, render
from bookshop.models import Book
from .cart import Cart


def add(request, id):
    cart = Cart(request)
    book = Book.objects.get(id=id)
    cart.add(book)
    return redirect('main') # указывается имя куда произойдет направление


def remove(request, id):
    cart = Cart(request)
    book = Book.objects.get(id=id)
    cart.remove(book)
    return redirect('cartView') # указывается имя куда произойдет направление


def view(request):
    cart = Cart(request)
    return render(request, 'cart.html',
                  {'cart':cart})
