from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Student


def students_list(request: HttpRequest) -> HttpResponse:
    template = 'school/students_list.html'
    ordering = 'group'
    context = {
        'object_list': Student.objects.order_by(ordering).all().prefetch_related('teachers'),
    }
    return render(request, template, context)
