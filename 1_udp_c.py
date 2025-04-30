from socket import socket, AF_INET, SOCK_DGRAM  # import socket api for udp at transport layer
BUFFER_SIZE = 2048  # define buffer size constant to avoid magic numbers

s = socket(AF_INET, SOCK_DGRAM)  # creating an instant of object socket sending as parameters 2 consts the convention is in capital letters the first one in which adress type and the second one means using udp

dst_ip = '127.0.0.1'  # set destination ip at network layer
dst_port = 12345  # set destination port at transport layer

s.settimeout(5)  # set timeout of 5 seconds so client wont hang forever

s.sendto(b'Hello', (dst_ip, dst_port))  # sendto sends udp message to using the sendto function of the socket class that recives 2 parameters the first one is the message and the second one is a tuple including the dst_ip dst_port i set before

data, sender_info = s.recvfrom(BUFFER_SIZE)  # setting max bytes i can receive in one message to BUFFER_SIZE

print(data.decode('utf-8'))  # the protocol of trnslating the data is text and in uft-8 style
print(sender_info)  # print sender ip and port

s.close()  # close socket to release port that other things could use it
