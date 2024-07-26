from django.db import models
from .validators import phone_number_validator, validate_instagram_url, validate_telegram_url
from phonenumber_field.modelfields import PhoneNumberField
from common.models import Media
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Contacts(models.Model):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, validators=[phone_number_validator])
    email = models.EmailField()
    location = models.URLField()

    class Meta:
        verbose_name = "Contacts"


class SocialMedia(models.Model):
    telegram = models.URLField(validators=[validate_telegram_url])
    facebook = models.URLField(validators=[])
    instagram = models.URLField(validators=[validate_instagram_url])
    linkedin = models.URLField(validators=[])

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Medias"


class ContactWithUs(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    message = models.TextField()

    class Meta:
        verbose_name = _("Contact With Us WEB")
        verbose_name_plural = _("Contact With Us WEB")


class AppInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()


class PrivacyPolicy(models.Model):
    text = models.TextField()

class Sponsor(models.Model):
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    url = models.CharField(max_length=255)

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, validators=[phone_number_validator])
    message = models.TextField()
    reason = models.ForeignKey('ContactWithUsReason', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _("Contact Us Mobile")
        verbose_name_plural = _("Contact Us Mobile")


class ContactWithUsCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Contact With Us Category")
        verbose_name_plural = _("Contact With Us Categories")

class ContactWithUsReason(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ContactWithUsCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Contact With Us Reason")
        verbose_name_plural = _("Contact With Us Reasons")