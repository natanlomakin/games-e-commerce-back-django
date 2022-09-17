from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Game, GameImages, GameSpecifications


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'


class GameImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameImages
        fields = '__all__'


class GameSpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSpecifications
        fields = '__all__'
