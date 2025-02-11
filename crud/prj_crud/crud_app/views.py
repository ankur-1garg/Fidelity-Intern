from django.shortcuts import render,redirect
from django.http import HttpResponse
from crud_app.forms import OrdersForm
from crud_app.models import Orders
from django.contrib import messages
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required


def orders(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data Saved')
    else:
        form = OrdersForm()
    return render(request, 'orders.html', {'form': form})


def showorders(request):
    orders = Orders.objects.all()
    return render(request, 'showorders.html', {'orders': orders})


def updateord(request, id):
    obj = Orders.objects.get(order_id=id)
    form = OrdersForm(instance=obj)
    if request.method == 'POST':
        form = OrdersForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('Data Updated')
    return render(request, 'order.html', {'form': form})


def deleteord(request, id):
    obj = Orders.objects.get(order_id=id)
    obj.delete()
    return HttpResponse('Data Deleted')


def setsession(request):
    request.session['name'] = 'steve'
    return HttpResponse('session is set')


def getsession(request):
    name = request.session.get('name', 'Guest')
    return HttpResponse(name)

def showstatic(request):
    return render(request, 'showstatic.html')

def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=uname).exists():
            messages.error(request, 'User not found')
        user=authenticate(request, username=uname, password=password)
        
        if user == None:
            messages.error(request, 'Invalid Credentials')
            
        else:
            auth_login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def register(request):
    return redirect('/home/')
def home(request):
    return render(request, 'home.html')    
        
        
                
                
            