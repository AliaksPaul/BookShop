from django.shortcuts import render
from .models import Author, Book


# def args(request):
#     visits = request.session.get('visits', 0)
#     request.session['visits'] = visits + 1

#     books_amount = Book.objects.count()
#     author_amount = Author.objects.count()
#     books = Book.objects.all()
#     return render(request, 'index.html', {'books': books,
#                                           'visits': visits, 
#                                           'books_amount': books_amount,
#                                           'author_amount': author_amount })

# def index(request):
#     visits = request.session.get('visits', 0)
#     request.session['visits'] = visits + 1
#     books_amount = Book.objects.count()
#     author_amount = Author.objects.count()
#     books = Book.objects.all()
#     return render(request, 'index.html', {'books': books,
#                                           'visits': visits, 
#                                           'books_amount': books_amount,
#                                           'author_amount': author_amount })


def book(request, id):
    book = Book.objects.get(id = id)

    visits = request.session.get('visits', 0)
    request.session['visits'] = visits
    books_amount = Book.objects.count()
    author_amount = Author.objects.count()


    return render(request, 'view.html', {'book': book, 'visits': visits,'books_amount': books_amount,'author_amount': author_amount })

def buy(request, id):
    book = Book.objects.get(id = id)

    visits = request.session.get('visits', 0)
    request.session['visits'] = visits
    books_amount = Book.objects.count()
    author_amount = Author.objects.count()

    return render(request, 'buy.html', {'book': book, 'visits': visits,'books_amount': books_amount,'author_amount': author_amount})
