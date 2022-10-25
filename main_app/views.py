from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
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

def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'description', 'years']
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