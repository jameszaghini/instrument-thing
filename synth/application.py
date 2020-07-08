import sys
import os.path
import subprocess
import mido
import rtmidi
import time
import serial
import signal

from .arduino import Arduino
from .key import Key

class Application():

    def __init__(self):

        signal.signal(signal.SIGINT, self.handler)

        self.performOperatingSystemCheck()
        self.performPythonVersionCheck()
        self.startFluidSynth()
        self.arduino = Arduino()
        self.run()

    def performOperatingSystemCheck(self):
        if not sys.platform.startswith('darwin'):
            raise Exception("Only macOS is supported")

    def performPythonVersionCheck(self):
        if sys.version_info < (3,8,3):
            raise Exception("Must be using Python 3.8.3")

    def startFluidSynth(self):
        basepath = os.path.dirname(__file__)
        # sf2 = os.path.abspath(os.path.join(basepath, '..', 'soundfonts', 'FUNKFRET.sf2'))
        sf2 = os.path.abspath(os.path.join(basepath, '..', 'soundfonts', 'FluidR3_GM.sf2'))
        subprocess.Popen(["fluidsynth", sf2], stdout=subprocess.DEVNULL)

    def getMidoPort(self):
        outputs = mido.get_output_names()
        first_port = outputs[0]
        return mido.open_output(first_port)

    def run(self):

        port = self.getMidoPort()

        keys = [
            Key(60, "A_DOWN", "A_UP"),
            Key(62, "B_DOWN", "B_UP"),
            Key(64, "C_DOWN", "C_UP"),
        ]

        print("♫ Ready.")

        while True:

            val = self.arduino.read()

            for key in keys:
                key.process(val)
                if key.play:
                    port.send(key.message)
                    key.play = False

    def handler(self, signum, frame):
        print("Bye")
        sys.exit()
