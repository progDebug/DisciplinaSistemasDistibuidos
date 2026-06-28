import zmq
import multiprocessing #-
from time import sleep #-
from const import IP_SERVER_2, PORT_SERVER_2

def client():
  context = zmq.Context()
  socket  = context.socket(zmq.REQ)       # create request socket

  socket.connect(f"tcp://{IP_SERVER_2}:{PORT_SERVER_2}") # block until connected
  socket.send(b"Hello world")             # send message
  message = socket.recv()                 # block until response
  socket.send(b"STOP")                    # tell server to stop
  print(message.decode())                 # print result
#-
if __name__ == "__main__": #-
  c = multiprocessing.Process(target=client) #-
#-
  sleep(2) #-
  c.start() #-
  c.join() #-
