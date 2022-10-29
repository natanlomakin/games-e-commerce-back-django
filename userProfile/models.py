from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profilePicture = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/')
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    zipCode = models.CharField(max_length=50, null=True, blank=True)
    dateOfBirth = models.CharField(max_length=50, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    fields = ['_id','user','profilePicture','country','city','street','zipCode','dateOfBirth']

    def __str__(self):
        return str(self._id)
