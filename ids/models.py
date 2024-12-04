from django.conf import settings
from django.db import models
from PIL import Image
import os
import uuid

class FoundID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='found_ids/')
    extracted_text = models.TextField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def image_url(self):
        # Returns the full URL of the image
        return self.image.url if self.image else None

    def __str__(self):
        return f"Image - {self.image}"

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    found_id = models.ForeignKey(FoundID, related_name='messages', on_delete=models.CASCADE)
    sender_contact = models.CharField(max_length=255, blank=True)
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    device_info = models.TextField(blank=True, null=True, help_text="Device or system information that sent the message.")

    def __str__(self):
        return f"Message from {self.sender_contact} on {self.sent_at}"
