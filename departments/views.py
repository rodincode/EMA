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
from .serializers import DepartmentsSerializer
import json
from django.db import connection

class CreateDept(CreateView):  
    model = Departments  
    form_class = AddDeptForm
    success_url = reverse_lazy('home')  
  
class RetrieveDept(ListView):  
    model = Departments   
    form_class = GetDeptForm
    success_url = reverse_lazy('/')  
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = Departments.objects.filter(dept_name__icontains=q)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(results=self.results, **kwargs)
        context["qs_json"] = json.dumps(list(Departments.objects.values()))
        return context
  
class RetrieveDeptAPI(APIView):
    def get(self, request):
        query = Departments.objects.all()
        serializer = DepartmentsSerializer(query, many=True)
        return Response(serializer.data)

class DeptDetail(DetailView):  
    model = Departments  
    success_url = reverse_lazy('/')  

  
class UpdateDept(UpdateView):  
    model = Departments  
    template_name_suffix = '_update_form'  
    fields = '__all__'  
    success_url = reverse_lazy('Dept')  
      
    # def get_success_url(self):  
          
      
      
class DeleteDept(DeleteView):  
    model = Departments  
    # here we can specify the URL   
    # to redirect after successful deletion  
    success_url = '/'     

print(connection.queries)