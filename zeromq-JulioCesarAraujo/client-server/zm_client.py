import zmq
import multiprocessing
from time import sleep
from zm_client import IP_SERVER, PORT_SERVER

def client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)

    socket.connect(f"tcp://{IP_SERVER}:{PORT_SERVER}")
    socket.send(b"Hello World")
    message = socket.recv()
    socket.send(b"STOP")
    print(message.decode())

if __name__ == "__main__": #-
    c = multiprocessing.Process(target=client) #-
    
    sleep(2) #-
    c.start() #-
    c.join() #-