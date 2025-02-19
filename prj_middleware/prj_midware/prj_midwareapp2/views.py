from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Manager
from django.db.models import Sum, Avg

# Function-based views
def manager_list(request):
    managers = Manager.objects.all()
    total_employees = Manager.objects.aggregate(Sum('manages'))['manages__sum']
    context = {
        'managers': managers,
        'total_employees': total_employees or 0
    }
    return render(request, 'prj_midwareapp2/manager_list.html', context)

def manager_detail(request, employee_id):
    manager = get_object_or_404(Manager, employee_id=employee_id)
    return render(request, 'prj_midwareapp2/manager_detail.html', {'manager': manager})

# Class-based views
class ManagerListView(ListView):
    model = Manager
    template_name = 'prj_midwareapp2/manager_list.html'
    context_object_name = 'managers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_employees'] = Manager.objects.aggregate(Sum('manages'))['manages__sum'] or 0
        context['avg_salary'] = Manager.objects.aggregate(Avg('salary'))['salary__avg'] or 0
        return context
