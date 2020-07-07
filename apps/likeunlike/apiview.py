from rest_framework import status
from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import (
    LikeSerializer,
    LikeToggleSerializer,
    IsLikedSerializer,
)
from .models import Like
from .services import user_likes_count



class LikeListAPIView(ListAPIView):
    """
    List API View to return all likes for authenticated user.
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('content_type__model', )

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                sender=self.request.user
            )
            .select_related('sender')
            .distinct()
        )


class LikeToggleView(CreateAPIView):
    """
    post:
    
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = LikeToggleSerializer

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        data['is_liked'] = bool(serializer.instance.pk)
        return Response(
            data,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data)
        )


class UserCountOfLikesAPIView(APIView):
    """
    API View to return count of likes for authenticated user.
    """
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return Response(
            data={'count': user_likes_count(request.user)}
        )



    
class IsLikedAPIView(GenericAPIView):
    """
    IsLikedAPIView
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = IsLikedSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(
            data={'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
