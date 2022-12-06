from django.db import models
from cart.models import Cart
from payment.models import PaymentMethod
from django.contrib.auth.models import User
from game.models import Game


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    total = models.IntegerField(blank=True, null=True)
    payment = models.ForeignKey(
        PaymentMethod, on_delete=models.SET_NULL, null=True)
    createdTime = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    fields = ['_id','user','cart','total','payment','createdTime']

    def __str__(self):
        return str(self._id)
