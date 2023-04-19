import socket
import pyaudio
import numpy as np
import struct

# bind all IP
# THARSIS/HOST = '192.168.0.101'
HOST = '192.168.1.206'
# 
# Listen on Port
PORT = 4210
#Size of receive buffer
BUFFER_SIZE = 1024
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the host and port

# THARSIS :UDP_IP = '192.168.0.108' # The IP that is printed in the serial monitor from the ESP32
#UDP_IP = '192.168.1.206' # The IP that is printed in the serial monitor from the ESP32

SHARED_UDP_PORT = 4210
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
#sock.connect((UDP_IP, SHARED_UDP_PORT))

CHUNK = 4096
WIDTH = 2
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5


p = pyaudio.PyAudio()

stream2 = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording")


s.bind((HOST, PORT))
stream = p.open(format=pyaudio.paInt16 , channels=1, rate=44100, output=True)

try:
    while True:
        #stream2.start_stream()

        #data2 = np.frombuffer(stream2.read(CHUNK,exception_on_overflow = False),dtype=np.int16)
        #data3=abs(data2)/32000*255
        #data3=data3.astype(np.int16)
        #print(data3)
        #stream2.stop_stream()


        #buf = struct.pack('<' + 'i' * len(data3), *data3)
        #sock.send(buf)
        stream.start_stream()
        data, addr = s.recvfrom(4096*2)  # buffer de 1024 bytes
        stream.write(data)


except KeyboardInterrupt:  # precionar Crtl + C para salir
    print("Cerrando...")
    stream.stop_stream()
    stream.close()
    p.terminate()
