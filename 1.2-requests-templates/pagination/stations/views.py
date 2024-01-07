import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator

# DATA = settings.BUS_STATION_CSV

def make_content(data) -> list:
    list_of_streets = []
    with open(data, encoding='utf-8') as file:
        result = csv.DictReader(file, delimiter=',')
        for row in result:
            list_of_streets.append(row)
    return list_of_streets

CONTENT = make_content('data-398-2018-08-30.csv')
print(CONTENT)

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request: HttpRequest) -> HttpResponse:
    page_number = request.GET.get('page', 1)
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
