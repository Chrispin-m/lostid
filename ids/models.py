from django.db import models
import uuid

class FoundID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='found_ids/')
    extracted_text = models.TextField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    found_id = models.ForeignKey(FoundID, related_name='messages', on_delete=models.CASCADE)
    sender_contact = models.CharField(max_length=255)
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
