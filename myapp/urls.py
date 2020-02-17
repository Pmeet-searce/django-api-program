from django.urls import path,include
from myapp import views

urlpatterns = [
    path('employees/',views.employees_list),
    path('employees/<int:pk>/',views.employees_detail)
]
