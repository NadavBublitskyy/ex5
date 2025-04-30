import socket  # import socket api for tcp at transport layer
BUFFER_SIZE = 4096  # define buffer size to avoid magic numbers

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating an instant of object socket sending as parameters 2 consts the first one in which adress type the second one means using tcp
dest_ip = '127.0.0.1'  # set server ip at network layer
dest_port = 12345  # set server port at transport layer
s.connect((dest_ip, dest_port))  # using the socket object function that receives the destination ip address and port for sending data and sets who i want to "talk to"

s.settimeout(5)  # set timeout of 5 seconds so client wont hang forever

msg = input("Message to send: ")  # a message for the user when he connects to the server
while not msg == 'quit':  # loop until user enters quit
    s.send(bytes(msg, 'utf-8'))  # using the sent function that can only sends bytes because it is tcp protocol and than converting the msg var i defined later into bytes usint the bytes function
    data = s.recv(BUFFER_SIZE)  # setting max bytes i can get to BUFFER_SIZE
    print("Server sent: ", data.decode('utf-8'))  # the protocol of trnslating the data is text and in uft-8 style
    msg = input("Message to send: ")  # a message for the user when he connects to the server

s.close()  # close socket to release port that other things could use it
