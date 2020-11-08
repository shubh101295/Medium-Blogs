from django.db import models

class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)

class Item(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	cost = models.IntegerField()