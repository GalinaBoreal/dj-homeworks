import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_number = int(request.GET.get('page', 1))
    content = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            content.append({'Name': item['Name'], 'Street': item['Street'], 'District': item['District']})

    paginator = Paginator(content, settings.ITEMS_PER_PAGE)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }

    return render(request, 'stations/index.html', context=context)
