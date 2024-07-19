from django.test import TestCase
from django.urls import reverse
from news.models import News
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
import datetime
import pytz
from unittest import mock

class TestNewsListView(APITestCase):
    url = reverse('news_list')

    def setUp(self):
        self.news1 = News.published.create(
            title="testnews",
            description="testnews",
            create_at=timezone.now(),
            # image="https://i.pinimg.com/236x/0b/11/81/0b11814a2a85126c755ce96d88593e1c.jpg"
        )
        self.news2 = News.published.create(
            title="testnews2",
            description="testnews2",
            create_at=timezone.now(),
            # image="https://i.pinimg.com/236x/0b/11/81/0b11814a2a85126c755ce96d88593e1c.jpg"
        )

    def test_happy(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 2)
