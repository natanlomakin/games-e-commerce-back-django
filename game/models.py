from platform import platform
from django.db import models
from django.contrib.auth.models import User

class gameImages(models.Model):
    imageOne = models.ImageField(null=True,blank=True,default='/placeholder.png')
    imageTwo = models.ImageField(null=True,blank=True,default='/placeholder.png')
    imageThree = models.ImageField(null=True,blank=True,default='/placeholder.png')
    imageFour = models.ImageField(null=True,blank=True,default='/placeholder.png')
    imageFive = models.ImageField(null=True,blank=True,default='/placeholder.png')
    _id=models.AutoField(primary_key=True,editable=False)
    fields =['_id','imageOne','imageTwo', 'imageThree','imageFour','imageFive']
    def __str__(self):
            return self._id 

class gameSpecifications(models.Model):
    osVersion = models.CharField(max_length=50,null=True,blank=True)
    cpu = models.CharField(max_length=50,null=True,blank=True)
    memory = models.CharField(max_length=50,null=True,blank=True)
    gpu = models.CharField(max_length=50,null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)
    fields =['_id','osVersion','cpu', 'memory','gpu']
    def __str__(self):
            return self._id 

class Game(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    description = models.CharField(max_length=50,null=True,blank=True)
    publisher = models.CharField(max_length=50,null=True,blank=True)
    developer = models.CharField(max_length=50,null=True,blank=True)
    platform = models.CharField(max_length=50,null=True,blank=True)
    image = models.ForeignKey(gameImages, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    specifications = models.ForeignKey(gameSpecifications, on_delete=models.CASCADE, null=True)
    key = models.URLField(max_length=200,null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)
    fields =['_id','description','price', 'title']
    def __str__(self):
            return self.title 


