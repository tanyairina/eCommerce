from django.db import models

# Create your models here.
class Product(models.Model):

    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

class Order(models.Model):
    items = models.CharField(max_length=1000)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    address_ship = models.CharField(max_length=1000)
    address_ship2 = models.CharField(max_length=1000, blank=True)
    city_ship = models.CharField(max_length=200)
    state_ship = models.CharField(max_length=200)
    zipcode_ship = models.CharField(max_length=200)
    total = models.CharField(max_length=200)


