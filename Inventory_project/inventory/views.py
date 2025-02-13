from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm, InventoryForm
from .models import Inventory

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, 'Account created successfully! You can now manage inventory items.')
            return redirect('inventory-list')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def inventory_list(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {
        'inventories': inventories,
        'user': request.user
    })


@login_required(login_url='login')
def inventory_detail(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    return render(request, 'inventory/inventory_detail.html', {'inventory': inventory})


@login_required(login_url='login')
def inventory_create(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.created_by = request.user
            inventory.save()
            messages.success(request, 'Inventory item created successfully!')
            return redirect('inventory-list')
    else:
        form = InventoryForm()
    return render(request, 'inventory/inventory_form.html', {'form': form, 'action': 'Create'})


@login_required(login_url='login')
def inventory_update(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inventory item updated successfully!')
            return redirect('inventory-list')
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'inventory/inventory_form.html', {'form': form, 'action': 'Update'})


@login_required(login_url='login')
def inventory_delete(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        inventory.delete()
        messages.success(request, 'Inventory item deleted successfully!')
        return redirect('inventory-list')
    return render(request, 'inventory/inventory_confirm_delete.html', {'inventory': inventory})
