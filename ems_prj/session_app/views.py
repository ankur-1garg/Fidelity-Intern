from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def session_home(request):
    return render(request, 'session_app/home.html')


def set_session(request):
    request.session['username'] = request.user.username
    request.session['last_visit'] = str(datetime.now())
    request.session.set_expiry(1000)
    return HttpResponse("Session data set!")


def get_session(request):
    username = request.session.get('username', 'Not set')
    last_visit = request.session.get('last_visit', 'Never')
    return HttpResponse(f"Username: {username}<br>Last visit: {last_visit}")
