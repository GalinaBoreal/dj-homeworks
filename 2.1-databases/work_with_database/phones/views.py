from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = {'name': 'name',
               'min_price': 'price',
               'max_price': '-price'}
    sort_get = request.GET.get('sort', 'name')
    phones = Phone.objects.order_by(sorting.get(sort_get))
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
