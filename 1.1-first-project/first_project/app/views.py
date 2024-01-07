import os

from datetime import datetime
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, reverse


def home_view(request: HttpRequest) -> HttpResponse:
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request: HttpRequest) -> HttpResponse:
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request: HttpRequest) -> HttpResponse:
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    work_dir = os.listdir()
    msg = f'Файлы в рабочей директории: {", ".join(work_dir)}'
    return HttpResponse(msg)
    # raise NotImplemented


