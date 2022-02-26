from django.db import models


# Create your models here.
class Item(models.Model):
    the_item = models.CharField(max_length=100)
    its_type = models.CharField(max_length=20)
