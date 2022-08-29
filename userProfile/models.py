from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    profilePicture = models.ImageField(null=True,blank=True,default='/placeholder.png')
    _id = models.AutoField(primary_key=True,editable=False)
    fields =['_id']
    def __str__(self):
            return self._id 