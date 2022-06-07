from socket import *
import time
from protocol_handler import *
from statistic_data import *

# Variáveis para controle.
host = '127.0.0.1'
port = 30000
size = 40
lost_packages = 0
pings = {} # Dicionário que terá o tempo de ida e chegada de cada um dos pings.
total_pings = 10
time_out = 1

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(time_out)

for j in range(total_pings): # Inicializando dicionário com listas vazias para cada um dos pings.
    pings['{:05d}'.format(j + 1)] = []

start = time.time() # Iniciando execução dos pings.

for i in range(total_pings):
    index = '{:05d}'.format(i + 1) # Número do ping com zeros a esquerda.
    time_client = '{:04d}'.format(int(time.time() * 1000) % 10000) # Tempo de ida com 4 bytes.

    pings[index].append(int(time.time() * 1000))

    message = index + '0' + time_client + 'filipe' + str(i + 1)

    print('[client] Enviando {}'.format(message))
    client_socket.sendto(message.encode(), (host, port))

    try:
        message, address = client_socket.recvfrom(size)
        message = message.decode()

        if is_valid_protocol(message):
            index, res, time_server, content = decode_protocol(message)

            if res == '1': # Recebeu pong.
                pings[index].append(int(time.time() * 1000)) # Volta.

                if pings[index][1] - pings[index][0] < time_out * 1000: # Verificando se chegou sem atraso.
                    print('[client] Recebido: ' + message)
                else:
                    print('[client] Recebido com atraso: ' + message)
            else:
                print('[client] Mensagem ({}) no formato do protocolo, mas resposta não é pong.'.format(message))
        else:
            print('[client] Mensagem ({}) invalida, ignorando pacote.'.format(message))
    except:
        print('[client] Mensagem {:05d} perdida'.format(i + 1))
        lost_packages = lost_packages + 1

end = time.time() # Fim da execução dos pings.

time_exec = (end - start) * 1000 # Tempo de execução em ms.

client_socket.close()

rtts = [] # Lista para armazenar todos os rtts para gerar as estatísticas.

for key in pings: # Preenchendo a lista de rtts usando os dados do dicionário.
    if len(pings[key]) == 2:
        rtts.append(pings[key][1] - pings[key][0])

print_datas(rtts, total_pings, time_exec)
