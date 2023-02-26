from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        task = Task(name=name, priority=priority)
        task.save()
    return render(request,'home.html')

