import subprocess
import mido
import rtmidi
import time
import serial
import sys
import serial.tools.list_ports

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
    sf2 = "/Users/jameszaghini/Downloads/FluidR3_GM/FluidR3_GM.sf2"
    subprocess.Popen(["fluidsynth", sf2], stdout=subprocess.DEVNULL)

def getMidoPort():
    outputs = mido.get_output_names()
    first_port = outputs[0]
    return mido.open_output(first_port)

def getSerialValue(serial):
    val = str(serial.readline())
    return val[2:][:-5]

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

    msg_a = mido.Message('note_on', note=60)
    msg_b = mido.Message('note_on', note=65)

    is_a_down = False
    is_b_down = False

    play_a = False
    play_b = False

    while True:

        val = getSerialValue(ser)

        if val == "A_DOWN":
            if not is_a_down:
                play_a = True
            is_a_down = True

        elif val == "A_UP":
            is_a_down = False

        if val == "B_DOWN":
            if not is_b_down:
                play_b = True
            is_b_down = True
            
        elif val == "B_UP":
            is_b_down = False

        if play_a:
            port.send(msg_a)
            play_a = False

        if play_b:
            port.send(msg_b)
            play_b = False

if __name__ == "__main__":
    main()
