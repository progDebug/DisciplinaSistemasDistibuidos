from socket import *
import pickle
from ConstMP import *

port = GROUPMNGR_TCP_PORT
membership = []

def handle_register(conn, req):
  membership.append((req["ipaddr"], req["port"]))
  print('Registered peer: ', req)

def handle_list(conn, req):
  peerList = [m[0] for m in membership]
  print('List of peers sent to server: ', peerList)
  conn.send(pickle.dumps(peerList))

def handle_unregister(conn, req):
  # to do
  pass

def handle_stop(conn, req):
  print("Stopping.")
  return True  # sinaliza ao serverLoop que deve parar

def handle_unknown(conn, req):
  print('Unknown operation received: ', req.get("op"))
  conn.send(pickle.dumps({"error": "unknown operation", "op": req.get("op")}))

HANDLERS = {
  "register": handle_register,
  "list": handle_list,
  "unregister": handle_unregister,
  "stop": handle_stop,
}

def serverLoop():
  serverSock = socket(AF_INET, SOCK_STREAM)
  serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
  serverSock.bind(('0.0.0.0', port))
  serverSock.listen(6)
  while True:
    (conn, addr) = serverSock.accept()
    msgPack = conn.recv(2048)
    req = pickle.loads(msgPack)

    handler = HANDLERS.get(req["op"], handle_unknown)
    stop = handler(conn, req)
    conn.close()

    if stop:
      serverSock.close()
      break

serverLoop()