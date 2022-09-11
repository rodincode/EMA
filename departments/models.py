from django.db import models

# Create your models here.
class Departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_location = models.CharField(max_length=100)
    dept_head = models.CharField(max_length=100)
    dept_budget = models.CharField(max_length=100)
    no_of_employees = models.IntegerField()
    