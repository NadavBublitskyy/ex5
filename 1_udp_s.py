from socket import socket, AF_INET, SOCK_DGRAM  # import socket api for udp at transport layer
BUFFER_SIZE = 2048  # define buffer size  to avoid magic numbers

s = socket(AF_INET, SOCK_DGRAM)  # creating an instant of object socket sending as parameters 2 consts the convention is in capital letters the first one in which adress type and the second one means using udp

src_ip = ''  # it doesn't matter do which network to bind
src_port = 12345  # set listening port at transport layer
s.bind((src_ip, src_port))  # bind socket to ip and port at transport layer

print(f"udp server listening on port {src_port}")  # printing that the server "is ready"

while True:  # infinite loop for the server to always receive requests from the user
    data, sender_info = s.recvfrom(BUFFER_SIZE)  # setting max bytes i can receive in one message to BUFFER_SIZE
    print(data.decode('utf-8'))  # the protocol of trnslating the data is text and in uft-8 style
    print(sender_info)  # print sender ip and port

    s.sendto(data.upper(), sender_info)  # sendto sends udp message to using the sendto function of the socket class that recives 2 parameters the first one is the message and the second one is a tuple including the dst_ip dst_port i set before
