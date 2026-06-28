import multiprocessing
import zmq, time
from Const import PORT_SERVER_1

def server():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(f"tcp://*:{PORT_SERVER_1}")
    while True:
        time.sleep(5)
        t = "TIME " + time.asctime()
        socket.send(t.encode())

if __name__ == "__main__":
    c = multiprocessing.Process(target=server)
    time.sleep(2)
    c.start()
    c.join()
        