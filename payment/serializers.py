from rest_framework import serializers
from .models import PaymentMethod

# The PaymentSerializer class is a ModelSerializer that serializes all fields of the PaymentMethod model
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
