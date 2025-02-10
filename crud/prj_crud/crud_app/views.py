from django.shortcuts import render
from django.http import HttpResponse
from crud_app.forms import OrdersForm
from crud_app.models import Orders


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
