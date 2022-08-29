from django.db import models
from django.contrib.auth.models import User

class PaymentMethod(models.Model):
    provider = models.CharField(max_length=50,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    expiration_date = models.CharField(max_length=2,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)
    fields =['_id','provider','expiration_date_month','expiration_date_year']
    def __str__(self):
            return self.provider


