from django.shortcuts import render
from app_tharsis.tasks import bluetooth_task, serial_task, pin_task

# Create your views here.


def data_view(request):
    # iniciar las tareas de Celery
    bluetooth_task.delay()
    serial_task.delay()
    pin_task.delay()
    
    # publicar los datos en MQTT
    publish.single("all_data", payload="Data collection started", hostname=settings.BROKER_ADDRESS)
    
    # renderizar la respuesta
    return render(request, 'data.html', {})
