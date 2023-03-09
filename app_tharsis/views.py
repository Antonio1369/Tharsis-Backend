from django.shortcuts import render
#from app_tharsis.tasks import bluetooth_task, serial_task, pin_task
from django.shortcuts import render

# Create your views here.

# Create your views here.

def index(request):
    return render(request, 'index.html', context={'text': 'Hola mundo'})

