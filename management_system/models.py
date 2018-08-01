from __future__ import unicode_literals
import uuid
from django.db import models

# Create your models here.


class Authentication(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.CharField(unique=True, max_length=256)
    password = models.CharField(max_length=256)

    class Meta:
        db_table = 'authentication'


class User(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    authentication = models.OneToOneField(Authentication, on_delete=models.CASCADE)
    salutation = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=512, null=True)
    date_of_birth = models.DateTimeField(null=True)
    relationship_status = models.CharField(max_length=128, null=True)
    gender = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = "user"


class UserAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(null=True)
    label = models.CharField(max_length=128, null=True)
    nearest_landmark = models.CharField(max_length=512, null=True)


    class Meta:
        db_table = "user_address"
