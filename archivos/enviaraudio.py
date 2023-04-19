"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).
"""

import pyaudio
import numpy as np
import struct
import time
import socket
UDP_IP = '162.168.1.48' # The IP that is printed in the serial monitor from the ESP32
SHARED_UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
sock.connect((UDP_IP, SHARED_UDP_PORT))

CHUNK = 4096
WIDTH = 2
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording")
##def get_rms( block ):
##    # RMS amplitude is defined as the square root of the 
##    # mean over time of the square of the amplitude.
##    # so we need to convert this string of bytes into 
##    # a string of 16-bit samples...
##
### we will get one short out for each 
### two chars in the string.
##count = len(block)/2
##format = "%dh"%(count)
##shorts = struct.unpack( format, block )
##
### iterate over the block.
##    sum_squares = 0.0
##    for sample in shorts:
##        # sample is a signed short in +/- 32768. 
##        # normalize it to 1.0
##        n = sample * SHORT_NORMALIZE
##        sum_squares += n*n
##
##    return math.sqrt( sum_squares / count )
##

while True:
    data = stream.read(CHUNK)  #read audio stream
    #amplitude=get_rms( data )
    sock.send(data)
    #data2 = np.frombuffer(stream.read(CHUNK,exception_on_overflow = False),dtype=np.int16)
    #mat = ( (data2 + 32700) / (32700 +32700) ) * (255 - 0) + 0
    
    #data3=abs(data2)/32767*255
    #data3=data2[data2<0]
    #data5=[]
##    for x in data2:
##        new_value = ( (x + 32700) / (32700 +32700) ) * (255 - 0) + 0
##        data5.append(new_value)
##    mat = np.array(data5)
##        
    #data3=((data2)+32767)/65534*255
    #data2=abs(data2)
    #data2=data2.astype(np.int16)
    #data3=data3.astype(np.int16)
    #mat=mat.astype(np.int16)
    #data1 = data2.astype(np.int16).tobytes()
    #print(data3)
    #buf = struct.pack('<' + 'i' * len(mat), *mat)
    #buf = struct.pack('<' + 'i' * len(data3), *data3)

    #sock.send(buf)
    #time.sleep(0.1/1000000)
    #data2=[]
    #stream.write(data1,CHUNK)  #play back audio stream
    
print("* done")

stream.stop_stream()
stream.close()

p.terminate()
