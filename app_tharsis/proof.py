import bluetooth

# Set up the Bluetooth connection
addr = "EC:94:CB:6F:3F:16"  # Replace with the ESP32 MAC address
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((addr, port))

# Continuously receive and print the potentiometer value

while True:
    data = sock.recv(1024)
    #print(type(data))
    #print("tipo de decode")
    #print(type(data.decode()))
    #print(data)
    print("Potentiometer value:", data.decode())
