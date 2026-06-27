# servidor_simples.py
import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('0.0.0.0', 5000))
servidor.listen(1)

print("Servidor aguardando conexão...")
conexao, endereco = servidor.accept()
print(f"Conectado a {endereco}")

while True:
    dados = conexao.recv(1024).decode()
    if not dados:
        break
    print(f"Mensagem: {dados}")
    conexao.send("OK".encode())

conexao.close()
servidor.close()