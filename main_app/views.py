from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def employees_index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html',{'employees': employees} )

def employees_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'employees/detail.html', {
        'employee': employee
    })


class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = '/employees' 
