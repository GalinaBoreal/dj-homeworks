from django.shortcuts import render, redirect
from books.models import Book
from django.core.paginator import Paginator
import datetime


def books_view(request):
    template = 'books/catalog.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def date_view(request, pub_date: datetime):
    template = 'books/pub_date.html'
    try:
        books = Book.objects.filter(pub_date=pub_date)
        content = list({book.pub_date.strftime('%Y-%m-%d') for book in Book.objects.all().order_by('pub_date')})
        page_number = content.index(pub_date.strftime('%Y-%m-%d')) + 1
        paginator = Paginator(content, 1)
        page = paginator.get_page(page_number)
        previous_page = paginator.get_page(page_number - 1).object_list[0]
        next_page = paginator.get_page(page_number + 1).object_list[0]
        context = {
            'books': books,
            'page': page,
            'previous_page': previous_page,
            'next_page': next_page
        }
    except ValueError:
        context = {
            'books': '',
        }

    # print(CONTENT, page_number)

    return render(request, template, context)
