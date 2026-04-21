from django.urls import path
from .views import RegisterView, TripListCreateView, TripDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('trips/', TripListCreateView.as_view(), name='trip-list-create'),
    path('trips/<int:pk>/', TripDeleteView.as_view(), name='trip-delete'),
]
