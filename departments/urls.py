from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RetrieveDept.as_view(), name='Dept'),
    path('add/', CreateDept.as_view(), name='AddDept'),
    path('info/', RetrieveDept.as_view(), name = 'DeptInfo'),
    path('api/', RetrieveDeptAPI.as_view(), name = 'DeptInfoAPI'),
    path('info/<int:pk>', DeptDetail.as_view(), name = 'DeptDetail') ,
    path('info/<int:pk>/update/', UpdateDept.as_view(), name = 'UpdateDept'),  
    path('info/<pk>/delete/', DeleteDept.as_view(), name = 'DeleteDept')  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
