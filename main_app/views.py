from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Employee, Language
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def employees_index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html',{'employees': employees} )

@login_required
def employees_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    languages_employee_doesnt_know = Language.objects.exclude(id__in = employee.languages.all().values_list('id'))
    return render(request, 'employees/detail.html', {
        'employee': employee,
        'languages': languages_employee_doesnt_know,
    })

@login_required
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


class EmployeeCreate(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['name', 'description', 'years']
    def form_valid(self,form):
        # Assigns the logged in user (self.request.user)
        form.instance.user = self.request.user 
        return super().form_valid(form)
    success_url = '/employees' 

class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ['description', 'years']

class EmployeeDelete(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = '/employees'

class LanguageList(LoginRequiredMixin, ListView):
    model = Language
    template_name = 'languages/index.html'

class LanguageCreate(LoginRequiredMixin, CreateView):
    model = Language
    fields = ('name', 'type')
    success_url = '/languages'