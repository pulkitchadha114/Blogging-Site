from enum import unique
from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class Service(models.Model):
    service_title = HTMLField(max_length=100)
    service_author = HTMLField(max_length=80)
    service_description = HTMLField()
    service_img = models.FileField(upload_to="service/", max_length=250, null=True, default=None)
    new_slug = AutoSlugField(populate_from='service_title', unique=True, null=True, default=None)