from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import  AllowAny

from .serializers import EmailSubscribeSerializer



class EmailSubscribeView(CreateAPIView):
    """
    post:
    
    """
    permission_classes = (AllowAny, )
    serializer_class = EmailSubscribeSerializer

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        data['is_active'] = serializer.instance.is_active
        return Response(
            data,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data)
        )