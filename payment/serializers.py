from rest_framework import serializers
from .models import PaymentMethod


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
