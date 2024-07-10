from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    id = models.PositiveIntegerField(primary_key=True)
    address = models.CharField(max_length=200)
    salary = models.BigIntegerField()
    max_salary = models.BigIntegerField()
    