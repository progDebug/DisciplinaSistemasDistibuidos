import zmq
import threading
import time
from Const import IP_SERVER_1, PORT_SERVER_2, PORT_SERVER_1

def server():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(f"tcp://*:{PORT_SERVER_2}")

    while True:
        mensagem = f"timestamp:{time.time()}"
        socket.send(mensagem.encode())
        time.sleep(1)

def client():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://{IP_SERVER_1}:{PORT_SERVER_1}")  # Conecta ao publisher local
    socket.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # Filtra por prefixo

    while True:
        mensagem = socket.recv_string()
        print(f"Recebido no SUB/PUB: {mensagem}")

if __name__ == "__main__":
    # Inicia as threads para publisher e subscriber
    thread_pub = threading.Thread(target=server)
    thread_sub = threading.Thread(target=client)

    thread_pub.start()
    thread_sub.start()

    thread_pub.join()
    thread_sub.join()