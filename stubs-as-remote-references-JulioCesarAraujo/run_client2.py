import pickle
from client import Client
from dbclient import DBClient
from constRPC import PORTC2, HOSTS, PORTS

c = Client(PORTC2, host='')   # escuta em todas as interfaces
print("Aguardando stub...")
data = c.recvAny()
dbC2 = pickle.loads(data)

dbC2.appendData('Client 2')
print("Valor final da lista:", dbC2.getValue())

# Envia STOP para o servidor
c.sendTo(HOSTS, PORTS, ['STOP'])   # ou use a constante STOP
