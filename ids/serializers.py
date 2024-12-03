from rest_framework import serializers
from .models import FoundID, Message
from django.conf import settings

class FoundIDSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = FoundID
        fields = ['id', 'image', 'image_url', 'extracted_text', 'posted_at']

    def get_image_url(self, obj):
        request = self.context.get('request')  
        if request and obj.image:
            return request.build_absolute_uri(obj.image.url)  
        return None

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'found_id', 'sender_contact', 'message_text', 'sent_at', 'device_info']
