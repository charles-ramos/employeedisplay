from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('employees/', views.employees_index, name='index'),
    path('employees/<int:employee_id>/', views.employees_detail, name='detail'),
    path('employees/create/', views.EmployeeCreate.as_view(), name='employees_create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employees_update'),
    path('employees/<int:pk>/delete/', views.EmployeeDelete.as_view(), name="employees_delete"),
    path('languages/', views.LanguageList.as_view(), name='languages_index'),
    path('languages/create/', views.LanguageCreate.as_view(), name='languages_create'),
    path('employees/<int:employee_id>/assoc_language/<int:language_id>/', views.assoc_language, name='assoc_language'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),


]