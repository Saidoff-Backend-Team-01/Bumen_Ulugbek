from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from company.models import ContactWithUs
from company.serializers import (ContactWithUsSerializer,FAQSerializer,SocialMediaSerializer, AppInfoSerializer,PrivacyPolicySerializer,SponsorSerializer,ContactsSerializer)
from .models import FAQ,SocialMedia,AppInfo,PrivacyPolicy,Sponsor,Contacts

class ContactWithUsView(CreateAPIView):
    queryset = ContactWithUs.objects.all()
    serializer_class = ContactWithUsSerializer


class ContactView(CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    


class FaqApiView(APIView):
    serializer_class = FAQSerializer

    def get(self, request, *args, **kwargs):
        try:
            seralizer = FAQSerializer(FAQ.objects.all(), many=True)
            return Response(seralizer.data, status=200)
        except Exception:
            return Response(data={"message": "Internal Server Error"}, status=500)


class SocialMediaView(CreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    
    
class AppInfoView(CreateAPIView):
    queryset = AppInfo.objects.all()
    serializer_class = AppInfoSerializer
    
    
class PrivacyPolicyView(CreateAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer
    
    
class SponsorView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer