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
