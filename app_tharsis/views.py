from django.shortcuts import render
#from app_tharsis.tasks import bluetooth_task, serial_task, pin_task
import paho.mqtt.publish as publish
from django.shortcuts import render
import numpy as np

from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.http import StreamingHttpResponse
import pyrealsense2 as rs
import numpy as np



# Create your views here.

# Create your views here.

def index(request):
    return render(request, 'index.html', context={'text': 'Hola mundo'})


def VideoCamera():
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.pose)
    config.enable_stream(rs.stream.fisheye, 1)
    config.enable_stream(rs.stream.fisheye, 2)
    profile = pipeline.start(config)

    def get_frame():
        frames = pipeline.wait_for_frames()
        fisheye_frame1 = frames.get_fisheye_frame(1)
        fisheye_image1 = cv2.cvtColor(np.asanyarray(fisheye_frame1.get_data()), cv2.COLOR_GRAY2BGR)
        fisheye_image1 = cv2.resize(fisheye_image1, (0, 0), fx=2, fy=2)
        ret, jpeg = cv2.imencode('.jpg', fisheye_image1)
        return jpeg.tobytes()

    return get_frame

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def monitor(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')

