import mido
import rtmidi
import time
import serial
import sys
import serial.tools.list_ports
import os

from .application import Application
from .key import Key
from .fluidsynthcontroller import FluidSynthController

def findPort():
    ports = list(serial.tools.list_ports.comports())
    port = next((x for x in ports if "Arduino" in x.description), None)
    if port == None:
        raise Exception("No Arduino found")
    return port.device

def getMidoPort():
    outputs = mido.get_output_names()
    first_port = outputs[0]
    return mido.open_output(first_port)

def getSerialValue(serial):
    line = serial.readline()
    line = line.rstrip()
    line = line.decode("utf-8")
    return line

def main():
    print("♪ Initialising.")

    Application()
    FluidSynthController.startFluidSynth()

    portDevice = findPort()

    ser = serial.Serial(portDevice, 9600)

    # TODO: how to get rid of this?
    time.sleep(1)
    print("♫ Ready.")

    port = getMidoPort()

    keys = [
        Key(60, "A_DOWN", "A_UP"),
        Key(62, "B_DOWN", "B_UP"),
        Key(64, "C_DOWN", "C_UP"),
    ]

    while True:

        val = getSerialValue(ser)

        for key in keys:
            key.process(val)
            if key.play:
                port.send(key.message)
                key.play = False

if __name__ == "__main__":
    main()
