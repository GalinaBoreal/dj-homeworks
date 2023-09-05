"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter

from books.views import books_view, index, books_pub_date
from books import converters

from books.views import books_view

register_converter(converters.DateConverter, 'yyyy-mm-dd')

urlpatterns = [
    path('books/', books_view, name='books'),
    path('', index),
    path('admin/', admin.site.urls),
    path('books/<yyyy-mm-dd:pub_date>/', books_pub_date, name='book_date')  # type: ignore
]
