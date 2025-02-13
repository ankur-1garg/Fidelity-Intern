# Import necessary modules from Django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm, InventoryForm
from .models import Inventory

# Create your views here.

# User registration view function
def register(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with POST data
        form = UserRegisterForm(request.POST)
        # Validate the form
        if form.is_valid():
            # Save the user to database
            user = form.save()
            # Log the user in
            login(request, user)
            # Display success message
            messages.success(request, 'Account created successfully! You can now manage inventory items.')
            # Redirect to inventory list page
            return redirect('inventory-list')
    else:
        # Create empty form for GET request
        form = UserRegisterForm()
    # Render registration template with form
    return render(request, 'registration/register.html', {'form': form})

# View to display all inventory items
def inventory_list(request):
    # Get all inventory objects from database
    inventories = Inventory.objects.all()
    # Render template with inventory list and user info
    return render(request, 'inventory/inventory_list.html', {
        'inventories': inventories,
        'user': request.user
    })

# View to display details of a specific inventory item
@login_required(login_url='login')  # Require login to access this view
def inventory_detail(request, pk):
    # Get inventory object or return 404 if not found
    inventory = get_object_or_404(Inventory, pk=pk)
    # Render template with inventory details
    return render(request, 'inventory/inventory_detail.html', {'inventory': inventory})

# View to create new inventory item
@login_required(login_url='login')  # Require login to access this view
def inventory_create(request):
    # Check if request method is POST
    if request.method == 'POST':
        # Create form instance with POST data
        form = InventoryForm(request.POST)
        # Validate form
        if form.is_valid():
            # Create inventory object but don't save yet
            inventory = form.save(commit=False)
            # Set the creator of the inventory item
            inventory.created_by = request.user
            # Save the inventory item
            inventory.save()
            # Display success message
            messages.success(request, 'Inventory item created successfully!')
            # Redirect to inventory list
            return redirect('inventory-list')
    else:
        # Create empty form for GET request
        form = InventoryForm()
    # Render form template
    return render(request, 'inventory/inventory_form.html', {'form': form, 'action': 'Create'})

# View to update existing inventory item
@login_required(login_url='login')  # Require login to access this view
def inventory_update(request, pk):
    # Get inventory object or return 404 if not found
    inventory = get_object_or_404(Inventory, pk=pk)
    # Check if request method is POST
    if request.method == 'POST':
        # Create form instance with POST data and existing inventory
        form = InventoryForm(request.POST, instance=inventory)
        # Validate form
        if form.is_valid():
            # Save the updated inventory
            form.save()
            # Display success message
            messages.success(request, 'Inventory item updated successfully!')
            # Redirect to inventory list
            return redirect('inventory-list')
    else:
        # Create form with existing inventory data
        form = InventoryForm(instance=inventory)
    # Render form template
    return render(request, 'inventory/inventory_form.html', {'form': form, 'action': 'Update'})

# View to delete inventory item
@login_required(login_url='login')  # Require login to access this view
def inventory_delete(request, pk):
    # Get inventory object or return 404 if not found
    inventory = get_object_or_404(Inventory, pk=pk)
    # Check if request method is POST
    if request.method == 'POST':
        # Delete the inventory item
        inventory.delete()
        # Display success message
        messages.success(request, 'Inventory item deleted successfully!')
        # Redirect to inventory list
        return redirect('inventory-list')
    # Render confirmation template
    return render(request, 'inventory/inventory_confirm_delete.html', {'inventory': inventory})
