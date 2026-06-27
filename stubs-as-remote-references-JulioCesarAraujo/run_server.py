from server import Server
from constRPC import PORTS

server = Server(PORTS, host="")
server.run()
