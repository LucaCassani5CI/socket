import socket 
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5006
BUFFER_SIZE = 1024

#Creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
primoNumero=float(input("Inserisci il primo numero: "))
operazione=input("Inserisci l'operazione {+,-,*,%}: ")
secondoNumero=float(input("Inserisci il secondo numero: "))
messaggio={'primoNumero':primoNumero,
'operazione':operazione,
'secondoNumero':secondoNumero}
messaggio=json.dumps(messaggio)
sock.sendto(messaggio.encode("UTF-8"), (SERVER_IP, SERVER_PORT))
data,addr=sock.recvfrom(BUFFER_SIZE)
print("Risultato: ",data.decode())

#Chiusura del socket
sock.close()