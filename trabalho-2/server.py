from socket import *
from protocol_handler import *

# Variáveis para controle.
recieve_host = '127.0.0.1'
recieve_port = 30000
size = 40

server_socket = socket(AF_INET, SOCK_DGRAM) # AF_INET: Protocolo IP, SOCK_DGRAM: Protocolo UDP.
server_socket.bind((recieve_host, recieve_port))

print('Server is running in port {}'.format(recieve_port))

while True:
    message, address = server_socket.recvfrom(size)
    message = message.decode()

    if is_valid_protocol(message):
        index, req, timestamp, content = decode_protocol(message)
        
        if req == '0': # Recebeu ping.
            print('Recieve: ' + message)
            res = '1'
            message = index + res + timestamp + content
            server_socket.sendto(message.encode(), address)
        else:
            print('[server] Mensagem no formato do protocolo, mas requisição não é ping.')
    else:
        print('[server] Mensagem invalida, ignorando pacote.')

server_socket.close()
