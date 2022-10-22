from platform import platform
from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    publisher = models.CharField(max_length=50, null=True, blank=True)
    developer = models.CharField(max_length=50, null=True, blank=True)
    platform = models.CharField(max_length=50, null=True, blank=True)
    imageOne = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/')
    imageTwo = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/')
    imageThree = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/')
    imageFour = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/')
    imageFive = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/')
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    createdTime = models.DateTimeField(auto_now_add=True)
    osVersion = models.CharField(max_length=50, null=True, blank=True)
    cpu = models.CharField(max_length=50, null=True, blank=True)
    memory = models.CharField(max_length=50, null=True, blank=True)
    gpu = models.CharField(max_length=50, null=True, blank=True)
    key = models.URLField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    fields = ['_id', 'description', 'price', 'title','imageOne','imageTwo','imageThree','imageFour','imageFive','osVersion','cpu','memory','gpu']

    def __str__(self):
        return self.title
