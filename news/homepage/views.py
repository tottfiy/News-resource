from django.shortcuts import render, get_object_or_404
from .models import News, Authors


def newspage_create(request, new_id):
    page = get_object_or_404(News, id=new_id)
    return render(request, 'homepage/news_article.html', {'page': page})


def author_create(request, new_id):
    auth = get_object_or_404(Authors, id=new_id)
    return render(request, 'homepage/authors_article.html', {'auth': auth})


def landing_handle(request):
    return render(request, 'homepage/landing.html')


def news_handle(request):
    return render(request, 'homepage/news.html')


def authors_handle(request):
    return render(request, 'homepage/authors.html')


def get_news(request):
    news = News.objects.order_by('-id')[:10]
    return render(request, 'homepage/landing.html', {'news': news})


def get_news_all(request):
    news = News.objects.order_by('-date')
    return render(request, 'homepage/news.html', {'news': news})


def get_authors(request):
    authors = Authors.objects.all()
    return render(request, 'homepage/authors.html', {'authors': authors})
