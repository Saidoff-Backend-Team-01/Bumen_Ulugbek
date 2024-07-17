from django.urls import path

from .views import NewsListView, NewsImageView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('newsimage/', NewsImageView.as_view(), name='newsimage'),
]