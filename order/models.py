from django.db import models
from cart.models import Cart
from payment.models import PaymentMethod

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    total = models.DecimalField(max_digits=5,decimal_places=2)
    payment = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, null=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)
    fields =['_id','total']
    def __str__(self):
            return self.total