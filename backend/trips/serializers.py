from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):
    city_description = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = [
            'id',
            'city',
            'departure_date',
            'departure_time',
            'created_at',
            'city_description',
            'image',
        ]
        read_only_fields = ['id', 'created_at', 'city_description', 'image']

    def get_city_description(self, obj):
        descriptions = {
            'Almaty': 'Mountains, lakes, cafes, city walks and nature trips.',
            'New York': 'Skyscrapers, Times Square, museums and fast city life.',
            'Tokyo': 'Modern technology, anime culture, temples and amazing food.',
            'Moscow': 'Historic architecture, Red Square, parks and museums.',
        }
        return descriptions.get(obj.city, '')

    def get_image(self, obj):
        images = {
            'Almaty': 'https://images.unsplash.com/photo-1541417904950-b855846fe074?auto=format&fit=crop&w=1200&q=80',
            'New York': 'https://images.unsplash.com/photo-1499092346589-b9b6be3e94b2?auto=format&fit=crop&w=1200&q=80',
            'Tokyo': 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=1200&q=80',
            'Moscow': 'https://images.unsplash.com/photo-1513326738677-b964603b136d?auto=format&fit=crop&w=1200&q=80',
        }
        return images.get(obj.city, '')
