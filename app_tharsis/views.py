from django.shortcuts import render
#from app_tharsis.tasks import bluetooth_task, serial_task, pin_task
import paho.mqtt.publish as publish
from django.shortcuts import render

# Create your views here.

# Create your views here.

def index(request):
    return render(request, 'index.html', context={'text': 'Hola mundo'})

def data_view(request):
    # iniciar las tareas de Celery
    bluetooth_task.delay()
    serial_task.delay()
    pin_task.delay()
    
    # publicar los datos en MQTT
    publish.single("all_data", payload="Data collection started", hostname=settings.BROKER_ADDRESS)
    
    # renderizar la respuesta
    return render(request, 'data.html', {})
