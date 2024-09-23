from django.shortcuts import render
from .models import News, Authors


# Create your views here.
def landing_handle(request):
    return render(request, 'homepage/landing.html')


def get_news(request):
    newslist = News.objects.all()
    return render(request, 'homepage/landing.html', {'news': newslist})


def get_authors(request):
    authorslist = Authors.objects.all()
    return render(request, 'homepage/landing.html', {'authors': authorslist})
