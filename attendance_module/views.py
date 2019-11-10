from django.shortcuts import render

# auth packages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def login_view(request):
    return render(request, 'attendance_module/user_login.html', {})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('attendance_system_app:user_dashboard'))
        else:
            return HttpResponse("Incorrect credentials")


def user_dashboard(request):
    context = {}
    return render(request, 'attendance_module/dashboard.html', context=context)
