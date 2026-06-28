import zmq
from const import PORT_SERVER_1
import multiprocessing
from time import sleep

def server():
    context = zmq.Context()
    socket  = context.socket(zmq.REP)    
    socket.bind(f"tcp://*:{PORT_SERVER_1}") 

    while True:
        message = socket.recv()
        if not "STOP" in str(message):
            reply = str(message.decode()+"*")
            socket.send(reply.encode())
        else:
            break

if __name__ == "__main__": #-
    c = multiprocessing.Process(target=server) #-
    
    sleep(2) #-
    c.start() #-
    c.join() #-