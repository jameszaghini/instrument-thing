import subprocess
import mido
import rtmidi
import time
import serial
import sys
import serial.tools.list_ports
import os

from .key import Key

def findPort():
    ports = list(serial.tools.list_ports.comports())
    port = next(x for x in ports if "Arduino" in x.description)
    return port.device

def performOperatingSystemCheck():
    if not sys.platform.startswith('darwin'):
        raise("Only macOS is supported")

def performPythonVersionCheck():
    if sys.version_info < (3,8,3):
        raise Exception("Must be using Python 3.8.3")

def startFluidSynth():
    basepath = os.path.dirname(__file__)
    # sf2 = os.path.abspath(os.path.join(basepath, '..', 'soundfonts', 'FUNKFRET.sf2'))
    sf2 = os.path.abspath(os.path.join(basepath, '..', 'soundfonts', 'FluidR3_GM.sf2'))
    subprocess.Popen(["fluidsynth", sf2], stdout=subprocess.DEVNULL)

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

    performOperatingSystemCheck()
    performPythonVersionCheck()
    startFluidSynth()

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
