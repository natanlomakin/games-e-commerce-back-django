from rest_framework import serializers
from .models import Profile

# The UserProfileSerializer class is a ModelSerializer that serializes all fields of the Profile model
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
