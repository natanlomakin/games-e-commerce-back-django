from rest_framework import serializers
from .models import Order

# The OrderSerializer class is a ModelSerializer that serializes all fields of the Order model
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
