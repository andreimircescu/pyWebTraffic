from httplib import HTTPConnection
import httpCommand
class httpConnection(HTTPConnection):

    def __init__(self,hostName, portNumber):

        HTTPConnection.__init__(self, hostName, portNumber)
        
        self._hostName   = hostName
        self._portNumber = portNumber
        self._commandList = []

    def addCommand(self, command):
        self._commandList.append(command)