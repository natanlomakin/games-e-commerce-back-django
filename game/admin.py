from django.contrib import admin
from .models import Game, gameSpecifications, gameImages

admin.site.register(Game)
admin.site.register(gameSpecifications)
admin.site.register(gameImages)
