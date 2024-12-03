from rest_framework import serializers
from .models import FoundID, Message

class FoundIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundID
        fields = ['id', 'image', 'extracted_text', 'posted_at']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'found_id', 'sender_contact', 'message_text', 'sent_at']
