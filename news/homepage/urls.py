from . import views
from django.urls import path


urlpatterns = [

    path('', views.get_news, name='homepage'),
    path('news', views.get_news_all, name='news'),
    path('news/<int:new_id>/', views.newspage_create, name='news_article'),
    path('authors/<int:new_id>/', views.author_create, name='authors_article'),
    path('authors', views.get_authors, name='authors'),
]