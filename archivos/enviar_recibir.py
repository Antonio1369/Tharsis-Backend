
import sounddevice as sd
import numpy as np
import socket

# Define las características del audio
freq = 44100
channels = 1
dtype = np.int16

# Conexión RTP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.1.208', 12345))  # La dirección IP de la Raspberry Pi
payload_type = 0x7F  # Tipo de carga útil arbitraria
seq_number = 0
timestamp = 0

# Inicia la reproducción de audio
with sd.RawStream(samplerate=freq, channels=channels, dtype=dtype, blocksize=1024) as stream:
    while True:
        # Recibe el paquete RTP
        rtp_packet, addr = sock.recvfrom(65536)
        # Desempaqueta los datos de RTP
        if len(rtp_packet) >= 12:
            version
