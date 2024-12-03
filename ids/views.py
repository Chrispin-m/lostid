from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import FoundID, Message
from .serializers import FoundIDSerializer, MessageSerializer
from .utils import extract_text_from_image

class PostFoundID(APIView):
    def post(self, request):
        image = request.FILES.get('image')
        if not image:
            return Response({"error": "Image is required"}, status=status.HTTP_400_BAD_REQUEST)

        found_id = FoundID.objects.create(image=image)
        # Extract text from image
        found_id.extracted_text = extract_text_from_image(found_id.image.path)
        found_id.save()

        return Response(FoundIDSerializer(found_id).data, status=status.HTTP_201_CREATED)

class SearchLostID(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        results = FoundID.objects.filter(extracted_text__icontains=query)
        return Response(FoundIDSerializer(results, many=True).data, status=status.HTTP_200_OK)

class PostMessage(APIView):
    def post(self, request, id):
        found_id = get_object_or_404(FoundID, id=id)
        data = request.data
        data['found_id'] = found_id.id
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
