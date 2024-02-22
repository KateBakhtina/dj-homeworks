from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


from articles.models import Article, Scope


def articles_list(request: HttpRequest) -> HttpResponse:
    template = 'articles/news.html'
    context = {
        'object_list': Article.objects.all().prefetch_related('scopes'),
    }
    return render(request, template, context)


