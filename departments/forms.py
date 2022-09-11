from django import forms
from .models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from employees.models import *

HEADS = set()
for i in Employees.objects.raw('SELECT id,employee_name FROM employees_employees WHERE employee_desg = "Chairman"'):
    HEADS.add(i.employee_name)

HEADS_LIST = []
for i in HEADS:
    HEADS_LIST.append((i,i))

DEPARTMENTS= [
    ('Content', 'Content'),
    ('Frontend', 'FrontEnd'),
    ('Backend', 'BackEnd'),
    ('Sales', 'Sales'),
    ('HR', 'HR'),
    ('Executive','Executive')
    ]

LOCATIONS= [
    ('Delhi', 'Delhi'),
    ('Bangalore', 'Bangalore'),
    ('Seattle', 'Seattle'),
    ('London', 'London'),
    ]

BUDGETS= [
    ('Less than 2 Cr', 'Less than 2 Cr'),
    ('Between 2 to 5 Cr', 'Between 2 to 5 Cr'),
    ('Between 5 to 15 Cr', 'Between 5 to 15 Cr'),
    ('More than 15 Cr', 'More than 15 Cr'),
    ]

class AddDeptForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = '__all__'
    dept_name = forms.CharField(label='Department', widget=forms. Select(choices=DEPARTMENTS))
    dept_location = forms.CharField(label='Location', widget=forms. Select(choices=LOCATIONS))
    dept_head = forms.CharField(label='Head', widget=forms. Select(choices=HEADS_LIST))
    dept_budget = forms.CharField(label='Estimated Budget', widget=forms. Select(choices=BUDGETS))
    no_of_employees = forms.IntegerField(label='Number of employees',validators=[MaxValueValidator(1000),MinValueValidator(10)])
    

class GetDeptForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = '__all__'
    dept_name = forms.CharField(label='Department', max_length=100)