# cliente_simples.py
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('192.168.0.8', 5000))  # Substitua pelo IP real

while True:
    msg = input("Mensagem: ")
    if msg.lower() == 'sair':
        break
    cliente.send(msg.encode())
    resposta = cliente.recv(1024).decode()
    print(f"Resposta: {resposta}")

cliente.close()