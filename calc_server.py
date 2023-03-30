import socket 
import json

SERVER_IP= "127.0.0.1"
SERVER_PORT = 5006 
BUFFER_SIZE = 1024

#Creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((SERVER_IP, SERVER_PORT))

print("Server in attesa di messaggi...")

while True:
  #ricezione dei dati dal client
    data, addr=sock.recvfrom(BUFFER_SIZE)
    if not data:
        break
    data=data.decode()
    data=json.loads(data)
    primoNumero=data['primoNumero']
    operazione=data['operazione']
    secondoNumero=data['secondoNumero']

    if operazione == '+':
        reply=primoNumero+secondoNumero
    elif operazione == '-':
        reply=primoNumero-secondoNumero
    elif operazione == '*':
        reply=primoNumero*secondoNumero
    elif operazione == '/':
        reply=primoNumero/secondoNumero
    else :
        reply=primoNumero%secondoNumero
    
    reply=str(reply)
    #invio di una risposta al client
    sock.sendto(reply.encode(), addr)