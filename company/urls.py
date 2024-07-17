from django.urls import path
from .views import *


urlpatterns = [
    path("contactus/", ContactWithUsView.as_view(), name="contact_with_us"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("faq/", FaqApiView.as_view(), name="faq"),
    path("socialmedia/", SocialMediaView.as_view(), name="socialmedia"),
    path("appinfo/", AppInfoView.as_view(), name="appinfo"),
    path("privacy_policy/", PrivacyPolicyView.as_view(), name="privacy_policy"),
    path("sponsor/", SponsorView.as_view(), name="sponsor"),
]