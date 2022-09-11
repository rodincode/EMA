from django.http import HttpResponse
from django.shortcuts import redirect, render  
from django.urls import reverse, reverse_lazy  
from django.contrib import messages  
from .models import *  
from .forms import *  
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView  
from django.views.generic.list import ListView  
from django.views.generic.detail import DetailView  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import EmployeesSerializer
import json
from django.db import connection

class Home(TemplateView):
    template_name = 'employees/home.html'

class CreateEmployee(CreateView):  
    model = Employees  
    form_class = AddEmployeeForm
    success_url = reverse_lazy('home')  
  
class RetrieveEmployee(ListView):  
    model = Employees  
    form_class = GetEmployeeForm
    success_url = reverse_lazy('/')  
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = Employees.objects.filter(employee_name__icontains=q)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(results=self.results, **kwargs)
        context["qs_json"] = json.dumps(list(Employees.objects.values()))
        return context
        
class RetrieveEmployeeAPI(APIView):
    def get(self, request):
        query = Employees.objects.all()
        serializer = EmployeesSerializer(query, many=True)
        return Response(serializer.data)

class EmployeeDetail(DetailView):  
    model = Employees  
    success_url = reverse_lazy('/')  

  
class UpdateEmployee(UpdateView):  
    model = Employees  
    template_name_suffix = '_update_form'  
    fields = '__all__'  
    success_url = reverse_lazy('')  
      
    # def get_success_url(self):  
          
      
      
class DeleteEmployee(DeleteView):  
    model = Employees   
    success_url = '/'     

print(connection.queries)