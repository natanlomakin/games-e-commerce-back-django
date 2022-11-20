from rest_framework import serializers
from .models import Wishlist

# The WishlistSerializer class is a ModelSerializer that serializes all fields of the Wishlist model
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'
