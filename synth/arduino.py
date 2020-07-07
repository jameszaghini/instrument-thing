import serial.tools.list_ports

class Arduino():

    def __init__(self):
        port = self.find_port()
        self.serial = serial.Serial(port, 9600)

    def find_port(self):
        ports = list(serial.tools.list_ports.comports())
        port = next((x for x in ports if "Arduino" in x.description), None)
        if port == None:
            raise Exception("No Arduino found")
        return port.device

    def read(self):
        line = self.serial.readline()
        line = line.rstrip()
        line = line.decode("utf-8")
        return line
