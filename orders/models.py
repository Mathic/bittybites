from django.db import models

# Create your models here.
class Order(models.Model):
	firstName = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	total = models.IntegerField(default=0)

class Flavors(models.Model):
	flavor = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	active = models.BooleanField(default=1)

class Macaron(models.Model):
	flavor = models.OneToOneField(Flavors, primary_key=True)
	quantity = models.IntegerField(default=3)
	order = models.ForeignKey(Order)
