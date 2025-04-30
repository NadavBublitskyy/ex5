import socket  # import socket api for tcp at transport layer
BUFFER_SIZE = 1024  # define buffer size to avoid magic numbers

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating an instant of object socket sending as parameters 2 consts the first one in which adress type the second one means using tcp
server_ip = ''  # set bind ip to all interfaces at network layer
server_port = 12345  # set listening port at transport layer
server.bind((server_ip, server_port))  # bind socket to ip and port at transport layer
server.listen(5)  # listen for up to 5 connection requests at transport layer

print(f"tcp server listening on port {server_port}")  # printing server "is ready"

while True:  # loop to accept each client
    client_socket, client_address = server.accept()  # accept new tcp connection and returns client socket and address
    print('connection from: ', client_address)  # display incoming connection info
    data = client_socket.recv(BUFFER_SIZE)  # setting max bytes i can get to BUFFER_SIZE
    while not data.decode('utf-8') == '':  # loop until client closes connection
        print('received: ', data.decode('utf-8'))  # the protocol of trnslating the data is text and in uft-8 style
        client_socket.send(data.upper())  # send uppercase data back to client
        data = client_socket.recv(BUFFER_SIZE)  # setting that i can get from this client max of BUFFER_SIZE

    print('client disconnected')  # when client disconnected print 'client disconnected'
    client_socket.close()  # close client socket to release port that other things could use it
