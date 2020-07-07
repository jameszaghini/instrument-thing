import os.path
import subprocess

class FluidSynthController():

    def __init__(self):
        print("FluidSynthController")

    @staticmethod
    def startFluidSynth():
        basepath = os.path.dirname(__file__)
        # sf2 = os.path.abspath(os.path.join(basepath, '..', 'soundfonts', 'FUNKFRET.sf2'))
        sf2 = os.path.abspath(os.path.join(basepath, '..', 'soundfonts', 'FluidR3_GM.sf2'))
        subprocess.Popen(["fluidsynth", sf2], stdout=subprocess.DEVNULL)
