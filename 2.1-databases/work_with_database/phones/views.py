from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort:
        choices = {
            'name': {'phones': Phone.objects.order_by('name').all()},
            'min_price': {'phones': Phone.objects.order_by('price').all()},
            'max_price': {'phones': Phone.objects.order_by('-price').all()},
        }
        context = choices.get(sort)
    else:
        context = {
            'phones': Phone.objects.all(),
        }
    return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug__exact=slug),
    }
    return render(request, template, context)


