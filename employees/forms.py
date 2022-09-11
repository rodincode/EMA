from django import forms
from .models import *
from django.core.validators import MaxValueValidator, MinValueValidator

GENDERS= [
    ('male', 'Male'),
    ('female', 'Female'),
    ('prefer not to say', 'Prefer not to say')
    ]

DESIGNATIONS= [
    ('Manager', 'Manager'),
    ('Developer', 'Developer'),
    ('Associate', 'Associate'),
    ('Trainee', 'Trainee'),
    ('VP', 'VP'),
    ('AVP', 'AVP'),
    ('Chairman','Chairman')
    ]

DEPARTMENTS= [
    ('Content', 'Content'),
    ('Frontend', 'FrontEnd'),
    ('Backend', 'BackEnd'),
    ('Sales', 'Sales'),
    ('HR', 'HR'),
    ('Executive','Executive')
    ]
    
class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'
    employee_name = forms.CharField(label='Name', max_length=100)
    employee_age = forms.IntegerField(label='Age',validators=[MaxValueValidator(60),MinValueValidator(20)])
    employee_gender = forms.CharField(label='Gender', widget=forms. Select(choices=GENDERS))
    employee_phone = forms.CharField(label='Mobile', max_length=100)
    employee_email = forms.EmailField(label='Email', max_length=100)
    employee_dept = forms.CharField(label='Department', widget=forms. Select(choices=DEPARTMENTS))
    employee_desg = forms.CharField(label='Designation', widget=forms. Select(choices=DESIGNATIONS))
    profile_pic = forms.ImageField(label='Profile Photo')
    verification_doc = forms.FileField(label='Document')
    

class GetEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'
    employee_name = forms.CharField(label='Name', max_length=100)