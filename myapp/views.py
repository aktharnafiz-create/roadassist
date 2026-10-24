from django.shortcuts import render, redirect
from .forms import BreakdownForm
from .models import Workshop

def home(request):
    return render(request, 'myapp/home.html')

def request_help(request):
    if request.method == 'POST':
        form = BreakdownForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BreakdownForm()
    return render(request, 'myapp/request_help.html', {'form': form})

def success(request):
    workshops = Workshop.objects.all()
    return render(request, 'myapp/success.html', {'workshops': workshops})