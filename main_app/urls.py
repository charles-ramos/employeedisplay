from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('employees/', views.employees_index, name='index'),
    path('employee/<int:employee_id>/', views.employees_detail, name='detail')
]