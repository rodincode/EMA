from django.db import models

# Create your models here.
class Employees(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_age = models.IntegerField()
    employee_gender = models.CharField(max_length=100)
    employee_phone = models.CharField(max_length=100)
    employee_email = models.EmailField(max_length=100)
    employee_dept = models.CharField(max_length=100)
    employee_desg = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile',blank=True)
    verification_doc = models.FileField(upload_to='pdf',default="")
    