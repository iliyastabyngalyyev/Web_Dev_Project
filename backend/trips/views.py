from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Trip
from .serializers import TripSerializer


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username', '').strip()
        password = request.data.get('password', '').strip()

        if not username or not password:
            return Response({'detail': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'detail': 'This username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create_user(username=username, password=password)
        return Response({'detail': 'User created successfully.'}, status=status.HTTP_201_CREATED)


class TripListCreateView(generics.ListCreateAPIView):
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TripDeleteView(generics.DestroyAPIView):
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)
