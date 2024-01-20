from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime

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

def show_books_by_date_view(request: HttpRequest, pub_date: datetime) -> HttpResponse:
    template = 'books/show_books.html'
    context = {
        'books': Book.objects.filter(pub_date__exact=pub_date)
    }
    return render(request, template, context)

