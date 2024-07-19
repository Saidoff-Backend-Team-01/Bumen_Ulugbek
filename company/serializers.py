from rest_framework import serializers
from .models import ContactWithUs,FAQ,Contacts,SocialMedia, AppInfo,PrivacyPolicy,Sponsor


class ContactWithUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactWithUs
        fields = ("name", "phone_number", "message")

    def create(self, validated_data):
        return ContactWithUs.objects.create(**validated_data)
    

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('address', 'phone_number', 'email', 'location')
        
    def create(self, validated_data):
        return Contacts.objects.create(**validated_data)
    

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ("question", "answer")
        # exlude = ("id",)



class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('telegram', 'facebook', 'instagram', 'linkedin')
        
    def create(self, validated_data):
        return SocialMedia.objects.create(**validated_data)

    
class AppInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppInfo
        fields = ('title', 'description')
        
    def create(self, validated_data):
        return AppInfo.objects.create(**validated_data)

    
class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ('text',)
        
    def create(self, validated_data):
        return PrivacyPolicy.objects.create(**validated_data)

    
class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('image', 'url')
        
    def create(self, validated_data):
        return Sponsor.objects.create(**validated_data)
