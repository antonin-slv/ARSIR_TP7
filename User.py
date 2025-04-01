import threading
import socket as sckt

def bertrand(port):
  def bertrand_behavior(port):
    # Bertrand choisit `b` sa clé privée
    b = 0

    socket = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)
    socket.bind(("127.0.0.1", port))
    
    socket.listen(True)
    
    print("Bertrand : initialized on port {}".format(port))
    print("Bertrand : Listening")
    conn, addr = socket.accept()

    print('Bertrand : Got new connection from {} at {}'.format(addr[0], addr[1]))
    
    # Bertrand attend qu'Arielle lui envoie
    ga = int(conn.recv(port).decode())
    print("Bertrand : Received {} from {}".format(ga, addr[1]))
    
    # Bertrand envoie à Arielle
    gb = 0
    print("Bertrand : Sending {} to {}".format(gb, addr[1]))
    conn.send(str(gb).encode())

    # Bertrand détermine la clé commune
    gab = 0
    print("Bertrand : calculated key : {}".format(gab))
    conn.close()
    print("Bertrand : Closing the connection from {} at {}".format(addr[0], addr[1]))
        
    socket.listen(False)
    socket.close()
    print("Bertrand : Disconnected")
    
  x = threading.Thread(target=bertrand_behavior, args=([port]))
  x.start()

  

def arielle(port):
  # Arielle choisit `a` sa clé privée
  a = 0

  socket = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)
  try :
    socket.connect(("127.0.0.1", port))
    print("Arielle {} : connected".format(socket.getsockname()[1]))
  except :
    print("Arielle : Connection Error")
    raise Exception

  

  # Arielle envoie à Bertrand
  ga = 0
  print("Arielle : Sending {} to {}".format(ga, port))
  socket.send(str(ga).encode())

  # Arielle attend que Bertrand lui envoie
  gb = int(socket.recv(port).decode())
  print("Arielle : Received {} from {}".format(gb, port))

  # Arielle détermine la clé commune
  gab = 0
  print("Arielle : calculated key : {}".format(gab))

  # Déconnexion du client
  socket.close()
  print("Arielle : Disconnected")
  
