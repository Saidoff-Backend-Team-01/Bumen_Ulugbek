from rest_framework import serializers
from django.conf import settings
from .models import Media

class MediaURlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('type', 'file')

    def to_representation(self, instance):
        """
        Convert the media instance into a representation that includes
        a URL to access the media file.
        """
        representation = super().to_representation(instance)
        request = self.context.get('request')
        file_url = instance.file.url if instance.file else None

        if file_url:
            if request:
                representation['file'] = request.build_absolute_uri(file_url)
            else:
                representation['file'] = f"{settings.HOST}{file_url}"
        return representation