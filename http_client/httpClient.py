import httplib
import time
from multiprocessing import Process

class httpClient(object):
    def __init__(self, hostName, portNumber, numberOfConnections = 1, duration = 60):
        self._hostName = hostName
        self._portNumber = portNumber
        self._numberOfConnections = numberOfConnections
        self._commandList = []
        self._connectionList = []
        self._duration = duration
        self.finalized = False

    def __setattr__(self, name, value):
        if name in self.__dict__ and self.finalized:
            print "Cannot change parameters when the http client is running"
        else:
            super(httpClient, self).__setattr__(name, value)

    def addCommand(self, commandType, page=""):
        command = (commandType,page)
        self._commandList.append(command)

    def run(self):
        self.finalized = True
        now = time.time()
        future = now + self._duration
        self._initializeConnections()
        self._establishConnections()
        while time.time() > future:
            pass

    def _initializeConnections(self):
        print "Initializing %s connection(s) ." % self._numberOfConnections
        for i in range(self._numberOfConnections):
            self._connectionList.append(httplib.HTTPConnection(self._hostName,self._portNumber))

    def _establishConnections(self):
        print "Establishing connections"
        for connection in self._connectionList:
            connection.connect()

if __name__=="__main__":
    testClient = httpClient("www.google.com",80,100)
    testClient.run()

