from django.shortcuts import render
from .models import employee
from django.db.models import Avg, Max, Min, Sum,Q

def employee_list(request):
    # Basic queryset operations
    all_employees = employee.objects.all()  # Get all employees
    ordered_employees = employee.objects.all().order_by('name')  # Order by name
    ordered_desc_salary = employee.objects.all().order_by('-salary')  # Order by salary descending
    
    # Filtering
    high_salary = employee.objects.filter(salary__gt=50000)  # Salary > 50000
    salary_range = employee.objects.filter(salary__range=(30000, 50000))  # Salary between 30000-50000
    
    # Aggregation
    total_salary = employee.objects.aggregate(Sum('salary'))
    avg_salary = employee.objects.aggregate(Avg('salary'))
    max_salary = employee.objects.aggregate(Max('salary'))
    
    context = {
        'employees': all_employees,
        'ordered_employees': ordered_employees,
        'high_salary_employees': high_salary,
        'salary_stats': {
            'total': total_salary['salary__sum'],
            'average': avg_salary['salary__avg'],
            'maximum': max_salary['salary__max']
        }
    }
    
    return render(request, 'prj_midwareapp/employee_list.html', context)