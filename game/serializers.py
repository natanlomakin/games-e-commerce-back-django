from rest_framework import serializers
from .models import Game

# The GameSerializer class is a ModelSerializer that serializes all fields of the Game model
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'