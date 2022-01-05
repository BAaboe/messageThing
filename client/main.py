import json
import socket
import threading

def jsonMaker(status, message):
    return json.dumps({"status": status, "message":message})

"""
1. Connect to server
2. Authenticate
3. Input -> Sent Messages
4. Recieve Messages
"""

class Client:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 5556
        self.name = ""

    def recv_msg(self):
        while True:
            data = json.loads(self.s.recv(1024).decode())
            if data["status"] == 110:
                msg = data["message"]
                if not msg.startswith(self.name):
                    print(msg)
            elif data["status"] == 500:
                break



    def send(self):
        while True:
            inp = input()

            if inp == ":exit":
                self.s.send(jsonMaker(500, "Disconnect").encode())
                break
            else:
                self.s.send(jsonMaker(111, inp+" ").encode())

    def connection_loop(self):
        recv_thread = threading.Thread(target=self.recv_msg, daemon=True)
        send_thread = threading.Thread(target=self.send)
        recv_thread.start()
        send_thread.start()

    
    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not self.name:
            self.name = input("Enter a name: ")
        
        self.s.connect((self.HOST, self.PORT))
        self.s.sendall(self.name.encode())
        data = self.s.recv(1024).decode()
        data = json.loads(data)
        if not data["status"] == 100:
            raise Exception("Somethin happend that shouldnt happen, good luck")

        self.connection_loop()


    def main(self):
        self.name = input("Enter a name: ")

        self.connect()

        
        
if __name__ == "__main__":
    c = Client()
    c.main()