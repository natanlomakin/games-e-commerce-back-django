from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import PaymentMethod


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
