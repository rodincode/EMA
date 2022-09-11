from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add_employee/', CreateEmployee.as_view(), name='AddEmployee'),
    path('employee_info/', RetrieveEmployee.as_view(), name = 'EmployeeInfo'),
    path('employee_api/', RetrieveEmployeeAPI.as_view(), name = 'EmployeeInfoAPI'),
    path('employee_info/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail') ,
    path('employee_info/<int:pk>/update/', UpdateEmployee.as_view(), name = 'UpdateEmployee'),  
    path('employee_info/<pk>/delete/', DeleteEmployee.as_view(), name = 'DeleteEmployee')  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
