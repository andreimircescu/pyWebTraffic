import urllib
class httpHeaders(object):
    def __init__(self):
        self._headers = {}

    def addHeader(self,header, headerValue):
        if header in self._headers:
            print "header %s is already added, overwritting." % header
        self._headers[header] = headerValue

    def getHeaders(self):
        return self._headers

class httpRequest(object):
    kRequestTypeGet = "GET"

    def __init__(self,requestType = kRequestTypeGet, request = "index.html"):
        self._requestType = requestType
        self._request =request

    def setRequest(self, requestType, request):
        self._requestType = requestType
        self._request = request

class httpParams(object):
    def __init__(self):
        self._params = {}

    def addParam(self,param, paramValue):
        if param in self._params:
            print "param %s is already added, overwritting." % param
        self._params[param] = paramValue

    def getParams(self):
        return urllib.urlencode(self._params)

class httpCommand(object):

    def __init__(self):
        self.httpHeaders = httpHeaders()
        self.httpParams = httpParams()
        self.request = httpRequest()

    def setRequest(self, requestType , request):
        self.request.setRequest(requestType, request)

    def addHeader(self, header, headerValue):
        self.httpHeaders.addHeader(header, headerValue)

    def addParam(self, param, paramValue):
        self.httpParams.addParam(param, paramValue)
