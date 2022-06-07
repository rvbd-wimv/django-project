from django.db import models

# Create your models here.

class CustomerType(models.Model):
    type_name=models.CharField(max_length=10)

    def __str__(self):
        return self.type_name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=10)
    postalcode = models.IntegerField(default=1000)
    contact_name = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    customer_type = models.ForeignKey('CustomerType', on_delete=models.DO_NOTHING)

