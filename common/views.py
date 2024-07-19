from django.shortcuts import render

# Create your views here.

from rest_framework.generics import CreateAPIView
from common.models import Media
from common.serializers import MediaURlSerializer

class MediaView(CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaURlSerializer   