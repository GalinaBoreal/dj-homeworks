from django.shortcuts import render, redirect
from books.models import Book
from django.core.paginator import Paginator


def books_view(request):
    books = Book.objects.filter(id__lte=2)
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)

def index(request):
    return redirect('books')


def books_pub_date(request, pub_date):
    book_date = Book.objects.filter(pub_date=pub_date).first()
    books_list = [obj for obj in Book.objects.order_by('pub_date')]
    template = 'books/pub_date.html'
    for num, obj in enumerate(books_list):
        if obj == book_date:
            paginator = Paginator(books_list, 1)
            page_number = num + 1
            page = paginator.get_page(page_number)
            previous_page_number = page.previous_page_number() if page.has_previous() else None
            previous_page = paginator.get_page(previous_page_number)
            previous_pub_date = previous_page.object_list[0].pub_date
            next_page_number = page.next_page_number() if page.has_next() else None
            next_page = paginator.get_page(next_page_number)
            next_pub_date = next_page.object_list[0].pub_date
            item = page.object_list[0]
            context = {
                'book_date': book_date,
                'page': page,
                'item': item,
                'previous_pub_date': previous_pub_date,
                'next_pub_date': next_pub_date,
            }
            return render(request, template, context)
