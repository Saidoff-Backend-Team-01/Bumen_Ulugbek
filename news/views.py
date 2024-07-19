from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import News,NewsImage
from .serializers import NewsListSerializer,NewsImageSerializer


class NewsListView(ListAPIView):
    queryset = News.published.all()
    serializer_class = NewsListSerializer

    def get_queryset(self):
        return self.queryset.order_by("-create_at")
    
class NewsImageView(ListAPIView):
    queryset = NewsImage.objects.all()
    serializer_class = NewsImageSerializer
    
    def get_queryset(self):
        return self.queryset.filter(news=self.kwargs["news_id"])
    