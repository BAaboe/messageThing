import threading
from request_handler import RequestHandler
import os
from Connection import Connection


def start():
    
    nw = RequestHandler()

    thread = threading.Thread(target=nw.connectio_thread, daemon=True)
    thread.start()

    while True:
        inp = input()
        if inp == "exit":
            nw.s.close()
            os._exit(0)
        elif inp == "connected":
            for i in nw.connected:
                print(i.name)
        

if __name__ == "__main__":
    start()