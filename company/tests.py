from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse


class TestContactWithUsView(APITestCase):

    def setUp(self):
        pass

    def test_happy(self):
        url = reverse('contact_with_us')
        data = {
            "name": "Test",
            "phone_number": " +998911234567",
            "message": "test"
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['name'], 'Test')
        self.assertEquals(list(response.data.keys()), ['name', 'phone_number', 'message'])