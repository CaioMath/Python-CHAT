from socket import *                                              #importação de todas as funções de 'socket'

c_server = "127.0.0.1"                                            #desta forma, servidor é a própria maquina que está executando (localhost)
c_door = 43210
obj_socket = socket(AF_INET, SOCK_STREAM)                         #cria-se o objeto socket, o primeiro parâmetro define a familia responsável por identificar os pacotes, neste caso, via DNS ou numero IP. Ja o segundo parâmetro representa o protocolo TCP (transporte do pacote)
obj_socket.bind((c_server, c_door))                               #associação no objeto socket com o servidor e porta
obj_socket.listen(2)                                              #indica que nesta aplicação o numero máximo de clientes é 2
print("Waiting for the customer....")
while True:
    con, client = obj_socket.accept()                             #laço para aguardar a chamado do cliente (accept() onde 'con' recebe a identificação da conexão e 'client' identificação do cliente
    print("Connected with: ", client)
    while True:
        msg_received = str(con.recv(1024))                        #aguarda-se uma solicitação em pacotes de 1024bytes
        print("We received: ", str(msg_received)[2:-1])           #print da mensagem recebida convertida a string e excluindo da string o "b'" padrão
        msg_sent = bytes(input("Your answer: "), 'utf-8')         #resposta em utf-8
        con.send((msg_sent))                                      #metodo 'send()' enviar a mensagem
        break                                                     #encerra o segundo laço
    con.close()                                                   #conexão fechada, aguardo da próxima