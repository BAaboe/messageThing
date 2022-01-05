

class Connection:
    def __init__(self, name, conn, addr, thread=None):
        self.name = name
        self.conn = conn
        self.addr = addr
        self.thread = thread

    def send(self, data):
        pass

    def getName(self):
         return self.name
    def setName(self, name):
        self.name = name

    def getConn(self):
        return self.conn
    def setConn(self, conn):
        self.conn = conn

    def getAddr(self):
        return self.addr
    def setAddr(self, addr):
        self.addr = addr

    def getThread(self):
        return self.thread
    def setThread(slef, thread):
        self.thread = thread

    