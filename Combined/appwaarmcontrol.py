#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PyAX-12

# The MIT License
#
# Copyright (c) 2010,2015 Jeremie DECOCK (http://www.jdhp.org)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
A PyAX-12 demo.

Move the first Dynamixel unit to various position angles.
This snippet moves the first Dynamixel unit to 0°, then -45°, -90°, -135°,
-150° (the maximum CW angle), +150° (the maximum CCW angle), +135°, +90°, +45°
and finally goes back to 0°.
"""

from pyax12.connection import Connection
from pyax12.argparse_default import common_argument_parser
import armcontrol
import bluetooth
import time


def main():
    # Defining Dynamixel IDs (Input for control)
    # Bluetooth Functions
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
                                service_classes=[
                                    uuid, bluetooth.SERIAL_PORT_CLASS],
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
            if not data:
                break
            print(data)
    # Do we want to implement check for busy arm and queue system for order drink?
    # We probably can do that by implementing a variable state which stores the number of drinks in queue and run a check
    # For non busy easy. For queue, arm would store the order and return to app queue number etc.
            data = data.decode('utf-8').split("\"")     # Formatting Output

            # Number of drinks
            n = int((len(data)-1)/6)
            print("Number of drinks", n)
            
            
            # Formatting Data for use
            arr =[]
            for x in range(1, len(data), 2):
                arr1 = [data[x]]
                arr = arr + arr1
                print(arr)          # Array of drinks e.g. [coffee,cold,0%,coffee,cold,0%]

            for x in range (1,n+1):
                print("Serving Drink ", x, arr[0+3*(x-1)])
                # Added timer delay for testing in app, please remove after added sequence for moving arm
                drink = arr[3*(x-1)]
                temp = arr[3*(x-1) + 1]
                sugar = arr[3*(x-1) + 2]
                print("Drink details:", drink, temp, sugar)

                print("Moving arm to ", drink, "dispenser")
                time.sleep(5)
                print("Dispensing Drink", x, drink)
                client_sock.send(("Dispensing Drink " + str(x) + ":" + drink).encode())
                time.sleep(5)
                print("Delivering Drink", x, drink)
                client_sock.send(("Delivering Drink " + str(x) + ":" + drink).encode())
                time.sleep(5)
                print("Delivered")
                client_sock.send(("Drink " + str(x) + " delivered").encode())
    except OSError:
        pass

    print("Disconnected.")

    client_sock.close()
    server_sock.close()
    print("All done.")


def turn(serial_connection):
    serial_connection.goto(3, 0, speed=512, degrees=True)
    serial_connection.goto(3, 45, speed=512, degrees=True)


if __name__ == '__main__':
    main()
