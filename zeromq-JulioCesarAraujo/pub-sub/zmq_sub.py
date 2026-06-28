import multiprocessing
import zmq, time
from zmq_pub import server
from Const import IP_SERVER_2, PORT_SERVER_2

def client():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://{IP_SERVER_2}:{PORT_SERVER_2}")
    socket.setsockopt(zmq.SUBSCRIBE, b"TIME")
    for i in range(5):
        time = socket.recv()
        print(time.decode())

if __name__ == "__main__":
    c = multiprocessing.Process(target=client)
    time.sleep(2)
    c.start()
    c.join()