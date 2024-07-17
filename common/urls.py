from django.urls import path
from common.views import MediaView


urlpatterns = [
    path('media/', MediaView.as_view(), name='media'),
]