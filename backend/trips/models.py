from django.contrib.auth.models import User
from django.db import models


class Trip(models.Model):
    CITY_CHOICES = [
        ('Almaty', 'Almaty'),
        ('New York', 'New York'),
        ('Tokyo', 'Tokyo'),
        ('Moscow', 'Moscow'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.city}'
