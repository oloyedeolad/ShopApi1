from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Person(AbstractUser):
    is_verified = models.BooleanField(default=False)


class Address(models.Model):
    description = models.TextField()
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    addressType = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.person)



class Payment(models.Model):
    cardNumber = models.CharField(max_length=20)
    cardPin = models.IntegerField(max_length=4)
    expiryDate = models.DateField()
    cardCode = models.IntegerField()
    balance = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.person)
