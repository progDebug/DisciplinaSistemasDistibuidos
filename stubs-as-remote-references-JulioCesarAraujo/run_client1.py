from dbclient import DBClient
from client import Client
from constRPC import HOSTS, PORTS, HOSTC2, PORTC2

dbC1 = DBClient(HOSTS, PORTS)
listID = dbC1.create()
dbC1.appendData('Client 1')
print(f"Lista criada com ID {listID}")

c1 = Client(0)   # porta não usada para escuta (pode ser qualquer uma)
c1.sendTo(HOSTC2, PORTC2, dbC1)
print("Stub enviado para cliente 2")
