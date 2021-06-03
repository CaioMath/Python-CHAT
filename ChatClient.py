from socket import *                                          #import de todas as funções de 'socket'

c_server = "127.0.0.1"                                        #o mesmo localhost, caso não fosse local é possível definir o IP de servido externo
c_door = 43210                                                #NECESSÁRIO que seja a mesma porta do servidor

while True:                                                   #laço para a continuidade do chat
    obj_socket = socket(AF_INET, SOCK_STREAM)                 #cria-se o objeto socket, o primeiro parâmetro define a familia responsável por identificar os pacotes, neste caso, via DNS ou numero IP. Ja o segundo parâmetro representa o protocolo TCP (transporte do pacote)
    obj_socket.connect((c_server, c_door))                    #conexão com o servidor por meio da função 'connect()'
    msg = bytes(input("Your message: "), 'utf-8')             #'msg' recebe a entrada do cliente convertida em bytes (socket transmite apenas tipo byte)
    obj_socket.send(msg)                                      #envio da mensagem
    answer = obj_socket.recv(1024)                            #recebe o dado enviado pelo servidor (limite para 1024 bytes)
    print("Server answer: ", str(answer)[2:-1])               #print da mensagem recebida excluido da string o "b'" padrão
    if str(msg)[2:-1].upper()=="STOP":                        #encerra a aplicação do lado do cliente, ja o servidor continuará recebendo ouytros clientes
        break
obj_socket.close()                                            #conexão fechada
