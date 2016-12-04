from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'base.html', {})

def dashboard(request):
    return render(request, 'front-end/src/app/pages/dashboard/dashboard.html', {})

