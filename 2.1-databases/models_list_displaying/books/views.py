from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date

from books.models import Book

def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

def show_books_view(request: HttpRequest) -> HttpResponse:
    template = 'books/show_books.html'
    context = {
        'books': Book.objects.all(),
    }
    return render(request, template, context)

def show_books_by_date_view(request: HttpRequest, pub_date: date) -> HttpResponse:
    template = 'books/show_books.html'
    dates_list = [object.pub_date for object in Book.objects.order_by('pub_date').distinct('pub_date').all()]
    date_index = dates_list.index(pub_date)
    try:
        next_date = dates_list[date_index + 1]
    except IndexError:
        next_date = pub_date
    if date_index - 1 < 0:
        previous_date = pub_date
    else:
        previous_date = dates_list[date_index - 1]
    books_by_date = Book.objects.filter(pub_date=pub_date)

    context = {
        'books': books_by_date,
        'len_of_dates_list': len(dates_list),
        'next_date_index': date_index + 1,
        'next_date': next_date,
        'previous_date_index': date_index - 1,
        'previous_date': previous_date,
    }
    return render(request, template, context)