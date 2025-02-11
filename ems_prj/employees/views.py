from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EmployeeRegistrationForm, EmployeeLoginForm


def register(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'emplyees/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = EmployeeLoginForm(request.POST)
#         if form.is_valid():
#             employee_id = form.cleaned_data['employee_id']
#             password = form.cleaned_data['password']
#             user = authenticate(employee_id=employee_id, password=password)

#             if user:
#                 login(request, user)
#                 return redirect('dashboard')
#             else:
#                 form.add_error(None, "Invalid credentials")
#         else:
#             print("Form is not valid")
#     else:
#         form = EmployeeLoginForm()
#     return render(request, 'emplyees/login.html', {'form': form})


# def user_login(request):
#     if request.method == 'POST':
#         form = EmployeeLoginForm(request.POST)
#         print(request.POST)  # Debug statement to check form data
#         if form.is_valid():
#             employee_id = form.cleaned_data['employee_id']
#             password = form.cleaned_data['password']
#             user = authenticate(employee_id=employee_id, password=password)

#             if user:
#                 login(request, user)
#                 return redirect('dashboard')
#             else:
#                 form.add_error(None, "Invalid credentials")
#         else:
#             print("Form is not valid")
#     else:
#         form = EmployeeLoginForm()
#     return render(request, 'emplyees/login.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        print(request.POST)  # Debug statement to check form data
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            password = form.cleaned_data['password']
            user = authenticate(employee_id=employee_id, password=password)

            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, "Invalid credentials")
        else:
            print("Form is not valid")
    else:
        form = EmployeeLoginForm()
    return render(request, 'emplyees/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'emplyees/dashboard.html')
