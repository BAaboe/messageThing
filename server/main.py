import threading
from request_handler import RequestHandler
import os


def start():
    
    nw = RequestHandler()

    thread = threading.Thread(target=nw.connectio_thread, daemon=True)
    thread.start()

    while True:
        inp = input()
        if inp == "exit":
            os._exit(0)
        

if __name__ == "__main__":
    start()