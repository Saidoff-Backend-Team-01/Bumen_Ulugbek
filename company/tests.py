from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from company.models import ContactWithUs, Contacts, FAQ, SocialMedia, AppInfo, PrivacyPolicy, Sponsor
from common.models import Media

class TestCompanyViews(APITestCase):

    def setUp(self):
        self.contact_with_us_url = reverse('contact_with_us')
        self.contact_url = reverse('contact')
        self.faq_url = reverse('faq')
        self.social_media_url = reverse('socialmedia')
        self.app_info_url = reverse('appinfo')
        self.privacy_policy_url = reverse('privacy_policy')
        self.sponsor_url = reverse('sponsor')

    def test_create_contact_with_us(self):
        data = {
            "name": "Test User",
            "phone_number": "+14155552671",
            "message": "This is a test message."
        }
        response = self.client.post(self.contact_with_us_url, data)
        if response.status_code != status.HTTP_201_CREATED:
            print("test_create_contact_with_us:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactWithUs.objects.count(), 1)

    def test_create_contact(self):
        data = {
            "address": "123 Test St",
            "phone_number": "998908615705",
            "email": "test@example.com",
            "location": "http://test.com/location"
        }
        response = self.client.post(self.contact_url, data)
        if response.status_code != status.HTTP_201_CREATED:
            print("test_create_contact:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contacts.objects.count(), 1)

    def test_get_faq(self):
        FAQ.objects.create(question="Test Question", answer="Test Answer")
        response = self.client.get(self.faq_url)
        if response.status_code != status.HTTP_200_OK:
            print("test_get_faq:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_social_media(self):
        data = {
            "telegram": "http://t.me/test",
            "facebook": "http://facebook.com/test",
            "instagram": "http://instagram.com/test",
            "linkedin": "http://linkedin.com/test"
        }
        response = self.client.post(self.social_media_url, data)
        if response.status_code != status.HTTP_201_CREATED:
            print("test_create_social_media:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SocialMedia.objects.count(), 1)

    def test_create_app_info(self):
        data = {
            "title": "Test App",
            "description": "This is a test app description."
        }
        response = self.client.post(self.app_info_url, data)
        if response.status_code != status.HTTP_201_CREATED:
            print("test_create_app_info:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AppInfo.objects.count(), 1)

    def test_create_privacy_policy(self):
        data = {
            "text": "This is a test privacy policy."
        }
        response = self.client.post(self.privacy_policy_url, data)
        if response.status_code != status.HTTP_201_CREATED:
            print("test_create_privacy_policy:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PrivacyPolicy.objects.count(), 1)

    def test_create_sponsor(self):
        media = Media.objects.create(file="test_file.jpg")
        data = {
            "image": media.id,
            "url": "https://i.pinimg.com/236x/0b/11/81/0b11814a2a85126c755ce96d88593e1c.jpg"
        }
        response = self.client.post(self.sponsor_url, data)
        if response.status_code != status.HTTP_201_CREATED:
            print("test_create_sponsor:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sponsor.objects.count(), 1)
