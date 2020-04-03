from django.db import models
from django.utils import timezone
# from djrichtextfield.models import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Vehicle(models.Model):
    vehicle_type=(('2 Wheeler','2 Wheeler'),
          ('4 Wheeler','4 Wheeler'))  
  
    Name = models.CharField(max_length=264,blank=True)
    Type = models.CharField(choices=vehicle_type,blank=True,max_length=264)
    image = models.ImageField(upload_to='img')
    content = RichTextUploadingField(blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    customerentry_updated_at = models.DateTimeField(auto_now=True)

