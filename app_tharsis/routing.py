from django.urls import path
from .consumers import GraphConsumer, VideoConsumer

ws_urlpatterns = [
    path('ws/graph/', GraphConsumer.as_asgi()),
    path('ws/video/', VideoConsumer.as_asgi()),
]