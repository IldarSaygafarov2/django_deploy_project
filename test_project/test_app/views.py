from django.shortcuts import render, get_object_or_404

from .models import Category, Article


def home_page(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'test_app/index.html', context)


def detail_page(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'article': article
    }
    return render(request, 'test_app/detail.html', context)
