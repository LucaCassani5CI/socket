import socket 
import json

SERVER_IP= "127.0.0.1"
SERVER_PORT = 65432
DIM_BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

    sock_server.bind((SERVER_IP, SERVER_PORT))

    sock_server.listen()

    print(f"server in ascolto su {SERVER_IP}:{SERVER_PORT}")

    while True:
        sock_service, address_client = sock_server.accept()

        with sock_service as sock_client:

            data = sock_client.recv(DIM_BUFFER).decode()
            data = json.loads(data)
            primoNumero = data["primoNumero"]
            operazione = data["operazione"]
            secondoNumero = data["secondoNumero"]
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
            reply = str(reply)
            print(f"Ricevuto messaggio dal client: {sock_client}, {data}")
            sock_client.sendall(reply.encode())