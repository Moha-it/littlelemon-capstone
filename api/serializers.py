from rest_framework import serializers
from restaurant.models import Menu, Booking

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']