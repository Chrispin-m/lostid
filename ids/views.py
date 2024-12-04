from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404
from .models import FoundID, Message
from .serializers import FoundIDSerializer, MessageSerializer
from .utils import extract_text_from_image
from rest_framework.parsers import MultiPartParser, FormParser

class FoundIDListView(ListAPIView):
    queryset = FoundID.objects.all()
    serializer_class = FoundIDSerializer

class FoundIDDetailView(RetrieveAPIView):
    queryset = FoundID.objects.all()
    serializer_class = FoundIDSerializer
    lookup_field = "id" 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoundID
from .serializers import FoundIDSerializer
import requests
from io import BytesIO
from PIL import Image

class PostFoundID(APIView):
    def post(self, request):
        # Get the uploaded image
        image = request.FILES.get('image')
        if not image:
            return Response({"error": "Image file is required"}, status=status.HTTP_400_BAD_REQUEST)
        found_id = FoundID.objects.create(image=image)

        image_url = found_id.image.url

        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status() 
            img = Image.open(BytesIO(response.content))
        except requests.exceptions.RequestException as e:
            return Response({"error": f"Failed to fetch the image: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": f"Failed to open the image: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        found_id.extracted_text = extract_text_from_image(img) 
        found_id.save()

        # Serialize the response
        serializer = FoundIDSerializer(found_id, context={'request': request})
        response_data = serializer.data
        response_data["message_link"] = f"/messages/{found_id.id}/"

        return Response(response_data, status=status.HTTP_201_CREATED)

class SearchLostID(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response({"error": "Search query is required"}, status=status.HTTP_400_BAD_REQUEST)
        results = FoundID.objects.filter(extracted_text__icontains=query).order_by('-posted_at')
        serializer = FoundIDSerializer(results, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostMessage(APIView):
    def post(self, request, id):
        found_id = get_object_or_404(FoundID, id=id)
        data = request.data
        data['found_id'] = found_id.id

        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            response_data = serializer.data
            response_data["found_id_link"] = f"/api/found_ids/{found_id.id}/"
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoundIDMessagesView(APIView):
    def get(self, request, id):
        found_id = get_object_or_404(FoundID, id=id)
        messages = Message.objects.filter(found_id=found_id)

        return Response(MessageSerializer(messages, many=True).data, status=status.HTTP_200_OK)
