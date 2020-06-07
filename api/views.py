from backend.models.subscribers import Subscriber
from backend.models.biography import Biography
from .serializers import SubscribersSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

class SubscribersListCreate(generics.ListCreateAPIView):
    """
    Interface for users to send their subscription data.
    """
    
    queryset = Subscriber.objects.all()
    serializer_class = SubscribersSerializer


class BiographyEndpoint(APIView):
    """
    Interface to get the biography set on the Admin side.
    """

    def get(self, request, format=None):
        """
        Returns the last bio object created.
        """

        biography = Biography.objects.latest(
                'created_at')

        serialized_bio = {
            'title': biography.title,
            'subtitle': biography.subtitle,
            'description': biography.description
        }
      
        return Response(serialized_bio)