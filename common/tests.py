from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from common.models import Media
import os

class TestCommonViews(APITestCase):

    def setUp(self):
        self.media_url = reverse('media')

        # Adjust the file paths to point to the media directory
        media_dir = os.path.join(os.path.dirname(__file__), 'media')

        self.image_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=open(os.path.join(media_dir, 'test_image.jpg'), 'rb').read(),
            content_type='image/jpeg'
        )
        self.video_file = SimpleUploadedFile(
            name='test_video.mp4',
            content=open(os.path.join(media_dir, 'test_video.mp4'), 'rb').read(),
            content_type='video/mp4'
        )
        self.audio_file = SimpleUploadedFile(
            name='test_audio.mp3',
            content=open(os.path.join(media_dir, 'test_audio.mp3'), 'rb').read(),
            content_type='audio/mp3'
        )

    def test_create_image_media(self):
        data = {
            'type': 'image',
            'file': self.image_file
        }
        response = self.client.post(self.media_url, data, format='multipart')
        if response.status_code != status.HTTP_201_CREATED:
            print("test_create_image_media:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Media.objects.count(), 1)

    def test_create_video_media(self):
        data = {
            'type': 'video',
            'file': self.video_file
        }
        response = self.client.post(self.media_url, data, format='multipart')
        if response.status_code != status.HTTP_201_CREATED:
            print("test_create_video_media:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Media.objects.count(), 1)

    def test_create_audio_media(self):
        data = {
            'type': 'audio',
            'file': self.audio_file
        }
        response = self.client.post(self.media_url, data, format='multipart')
        if response.status_code != status.HTTP_201_CREATED:
            print("test_create_audio_media:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Media.objects.count(), 1)

    def test_create_invalid_media_type(self):
        data = {
            'type': 'invalid_type',
            'file': self.image_file
        }
        response = self.client.post(self.media_url, data, format='multipart')
        if response.status_code != status.HTTP_400_BAD_REQUEST:
            print("test_create_invalid_media_type:", response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Media.objects.count(), 0)
