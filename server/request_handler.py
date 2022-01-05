
import socket 
from Connection import Connection
import threading
import json

def jsonMaker(self, status, message):
        return json.dumps({"status": status, "message":message})


class RequestHandler():

    def __init__(self):
        self.connected = []

    def broacast(self, data):
        for i in self.connected:
            i.conn.send(jsonMaker(110, data).encode())
            recv = conn.recv(2048).decode()
            if recv != 100:
                print("ehh, something is wrong")



    
    def connection_loop(self, connection):
        while True:
            recv = conn.recv(2048).decode()
            data = json.loads(recv)

            if data["status"] == 111:
                self.broacast(data["message"])
            


    def authentication(self, conn, addr):
        try:
            data = conn.recv(1024)
            name = str(data.encode())
            if not name:
                raise Exception("No name recived")

            conn.send(jsonMaker(100, "Connected"))

            connection = Connection(name, conn, addr)

        except socket.error as e:
            print(e)
        print(f"{name} connected")

        thread = threading.Thread(target=self.connection_loop, daemon=True, args=(connection,))
        
        connection.setThread(thread)
        self.connected.append(connection)

        thread.start()


    def connectio_thread(self):
        server = ""
        port = 5556

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((server, port))
        except socket.error as e:
            str(e)
        
        s.listen(1)
        print("Waiting for connections")

        while True:
            conn, addr = s.accept()
            print("New connection")

            self.authentication(conn, addr)

        self.close()