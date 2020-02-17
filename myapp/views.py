from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Employees
from .serializers import EmployeeSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

def index(req):
    index_str="Hello World!, To checkout the restful APIs go to /employees_list/ for GET and POST and go to /employees_detail/<number>/ to get detail of a particular employee  "
    return HttpResponse(index_str)

@csrf_exempt
def employees_list(req):

    if req.method == "GET":
        employees = Employees.objects.all()
        serializer = EmployeeSerializers(employees,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif req.method == "POST":
        data = JSONParser().parse(req)
        serializer = EmployeeSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def employees_detail(req,pk):
    
    try:
        employee = Employees.objects.get(pk=pk)
    except Employees.DoesNotExist:
        return HttpResponse(status=404)
    
    if req.method == "GET":
        serializer = EmployeeSerializers(employee)
        return JsonResponse(serializer.data,safe=False)
    elif req.method == "PUT":
        data = JSONParser().parse(req)
        serializer = EmployeeSerializers(employee,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    elif req.method == "DELETE":
        employee.delete()
        return HttpResponse(status=204)
