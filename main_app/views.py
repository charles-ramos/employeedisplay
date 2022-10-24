from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee, Language
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
    languages_employee_doesnt_know = Language.objects.exclude(id__in = employee.languages.all().values_list('id'))
    return render(request, 'employees/detail.html', {
        'employee': employee,
        'languages': languages_employee_doesnt_know,
    })

def assoc_language(request, employee_id, language_id):
    Employee.objects.get(id=employee_id).languages.add(language_id)
    return redirect('detail', employee_id=employee_id)

class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = '/employees' 

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'description', 'years']

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = '/employees'

class LanguageList(ListView):
    model = Language
    template_name = 'languages/index.html'

class LanguageCreate(CreateView):
    model = Language
    fields = ('name', 'type')
    success_url = '/languages'