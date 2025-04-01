import threading
import socket as sckt
import Toolbox

def bertrand(port,g,p,b):
  def bertrand_behavior(port,g,p,b):

    # Bertrand choisit `b` sa clé privée ( dans les parametres)

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
    gb = Toolbox.exp(g,b,p)
    print("Bertrand : Sending {} to {}".format(gb, addr[1]))
    conn.send(str(gb).encode())

    # Bertrand détermine la clé commune
    gab = Toolbox.exp(ga,b,p)
    print("Bertrand : calculated key : {}".format(gab))
    conn.close()
    print("Bertrand : Closing the connection from {} at {}".format(addr[0], addr[1]))
        
    socket.listen(False)
    socket.close()
    print("Bertrand : Disconnected")
    
  x = threading.Thread(target=bertrand_behavior, args=([port,g,p,b]))
  x.start()

  

def arielle(port,g,p,a):
  # Arielle choisit `a` sa clé privée (dans les parametres)

  socket = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)
  try :
    socket.connect(("127.0.0.1", port))
    print("Arielle {} : connected".format(socket.getsockname()[1]))
  except :
    print("Arielle : Connection Error")
    raise Exception

  

  # Arielle envoie à Bertrand
  ga = Toolbox.exp(g,a,p)
  print("Arielle : Sending {} to {}".format(ga, port))
  socket.send(str(ga).encode())

  # Arielle attend que Bertrand lui envoie
  gb = int(socket.recv(port).decode())
  print("Arielle : Received {} from {}".format(gb, port))

  # Arielle détermine la clé commune
  gab = Toolbox.exp(gb,a,p)
  print("Arielle : calculated key : {}".format(gab))

  # Déconnexion du client
  socket.close()
  print("Arielle : Disconnected")
  
