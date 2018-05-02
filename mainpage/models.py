from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.TextField()
    email = models.TextField()
    age = models.IntegerField()


class PureCustomer(models.Model):
    name = models.TextField()
    email = models.TextField()
    age = models.IntegerField()

    class Meta:
        db_table = "customer"
