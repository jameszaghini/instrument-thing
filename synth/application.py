import sys

class Application():

    def __init__(self):
        self.performOperatingSystemCheck()
        self.performPythonVersionCheck()

    def performOperatingSystemCheck(self):
        if not sys.platform.startswith('darwin'):
            raise Exception("Only macOS is supported")

    def performPythonVersionCheck(self):
        if sys.version_info < (3,8,3):
            raise Exception("Must be using Python 3.8.3")
