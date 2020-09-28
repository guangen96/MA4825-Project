#!/usr/bin/env python3
"""PyBluez simple example rfcomm-server.py

Simple demonstration of a server application that uses RFCOMM sockets.

Author: Albert Huang <albert@csail.mit.edu>
$Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $
"""

import bluetooth
import time

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE],
                            # protocols=[bluetooth.OBEX_UUID]
                            )

print("Waiting for connection on RFCOMM channel", port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)
# After connected to device receive data and print data
# we need to integrate the app we will be developing to the data here
# We might need another way to bluetooth connect, not sure how the mit app inventor bluetooth connection work, but should work
# Refer to https://github.com/pybluez/pybluez for more examples and more functions that we can use

try:
    while True:
        data = client_sock.recv(1024)
        data2 = "coffee hot no"
# Do we want to implement check for busy arm and queue system for order drink? 
# We probably can do that by implementing a variable state which stores the number of drinks in queue and run a check
# For non busy easy. For queue, arm would store the order and return to app queue number etc.
        drink = data.split()[0]
        temp = data.split()[1]
        sugar = data.split()[2]

        print("Received", data, drink, temp, sugar)
        if not data:
            break
        
        # Added timer delay for testing in app, please remove after added sequence for moving arm
        if drink == b"coffee":
            print("Run Sequence for moving arm to coffee dispenser")
            time.sleep(2)
            client_sock.send("Preparing Coffee".encode())
        elif drink == b"tea":
            print("Run Sequence for moving arm to tea dispenser")
            time.sleep(2)
            client_sock.send("Preparing Tea".encode())
        else:
            print("Run Sequence for moving arm to milo dispenser")
            time.sleep(2)
            client_sock.send("Preparing Milo".encode())
        # Add if else for temp if needed for ice
        # Add if else for sugar if needed for ice
        time.sleep(2)
        # Sending message to app once drinks are delivered (Please add sequence to move arm to delivery place)
        client_sock.send("Drink Delivered".encode())
except OSError:
    pass

print("Disconnected.")

client_sock.close()
server_sock.close()
print("All done.")
