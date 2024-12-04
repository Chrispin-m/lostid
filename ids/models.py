from django.conf import settings
from django.db import models
from PIL import Image
import os
import uuid
from cloudinary.models import CloudinaryField

class FoundID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = CloudinaryField('image')
    image_absolute_url = models.URLField(max_length=500, blank=True, null=True)  # Field to store absolute URL
    extracted_text = models.TextField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.image and not self.image_absolute_url:
            self.image_absolute_url = self.image.url 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image - {self.image_absolute_url if self.image_absolute_url else 'No Image'}"

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    found_id = models.ForeignKey(FoundID, related_name='messages', on_delete=models.CASCADE)
    sender_contact = models.CharField(max_length=255, blank=True)
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    device_info = models.TextField(blank=True, null=True, help_text="Device or system information that sent the message.")

    def __str__(self):
        return f"Message from {self.sender_contact} on {self.sent_at}"
