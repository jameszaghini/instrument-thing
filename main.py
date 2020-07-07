import subprocess
import mido
import rtmidi
import time
import serial

# TODO what if no ports, how to find port we're interested in?

def main():
    print("♪ Initialising.")

    ser=serial.Serial('/dev/cu.usbmodem141301', 9600)

    sf2 = "/Users/jameszaghini/Downloads/FluidR3_GM/FluidR3_GM.sf2"

    subprocess.Popen(["fluidsynth", sf2], stdout=subprocess.DEVNULL)

    # TODO: how to get rid of this?
    time.sleep(1)
    print("♫ Ready.")

    outputs = mido.get_output_names()

    first_port = outputs[0]

    port = mido.open_output(first_port)

    msg_a = mido.Message('note_on', note=60)
    msg_b = mido.Message('note_on', note=65)

    is_a_down = False
    is_b_down = False

    play_a = False
    play_b = False

    while True:

        val = str(ser.readline())
        val = val[2:][:-5]

        # print(val)

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
