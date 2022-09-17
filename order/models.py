from django.db import models
from cart.models import Cart
from payment.models import PaymentMethod
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    payment = models.ForeignKey(
        PaymentMethod, on_delete=models.CASCADE, null=True)
    createdTime = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    fields = ['_id', 'total', 'user', 'cart', 'payment']

    def __str__(self):
        return str(self._id)
