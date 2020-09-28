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

from pyax12.connection import Connection
#from pyax12.argparse_default import common_argument_parser
#import pyax12.packet as pk

import time

def main():

    # Connect to the serial port 
    serial_connection = Connection(port='COM4', baudrate=25000, timeout=0.1, rpi_gpio=False)
    
    # Dynamixels ID: Can be changed with Dynamixel Wizard (Refer to Briefing on Dynamixels PDF)
    # Base: 5 (Angled labelled on base)
    # Next: 0 (Input reference for easier)
    # Next: 4 (Input reference for easier)
    # Last: 1 (Input reference for easier)

    # Testing (Straight position)
    serial_connection.goto(5, 0, speed=200, degrees=True)
    time.sleep(2)
    serial_connection.goto(0, 0, speed=200, degrees=True)
    time.sleep(2)
    serial_connection.goto(4, 0, speed=200, degrees=True)
    time.sleep(2)
    serial_connection.goto(1, 0, speed=200, degrees=True)
    time.sleep(2)
    
    # Testing all at 90 degrees 
    serial_connection.goto(5, 10, speed=200, degrees=True)
    time.sleep(2)
    serial_connection.goto(0, 10, speed=200, degrees=True)
    time.sleep(2)
    serial_connection.goto(4, 10, speed=200, degrees=True)
    time.sleep(2)
    serial_connection.goto(1, 10, speed=200, degrees=True)
    time.sleep(2)
    # testing all at 90 degrees
    serial_connection.goto(5, 0, speed=200, degrees=True)
    time.sleep(2)
    serial_connection.goto(0, 0, speed=200, degrees=True)
    time.sleep(2)
    serial_connection.goto(4, 0, speed=200, degrees=True)
    time.sleep(2)
    serial_connection.goto(1, 0, speed=200, degrees=True)
    time.sleep(2)

    # Close the serial connection
    serial_connection.close()

if __name__ == '__main__':
    main()
