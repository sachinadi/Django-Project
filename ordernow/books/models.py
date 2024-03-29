from django.db import models

# Create the class for the objects you want to store in database
class Inventory(models.Model):
    id = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length=255)
    isbn_id = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    publisher = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    quantity = models.IntegerField()
    author= models.CharField(max_length = 255)  