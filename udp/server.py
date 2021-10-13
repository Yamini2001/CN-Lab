import socket 
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = "127.0.0.1"
port = 9999
sock.bind((host,port))
while True:
    data , addr=sock.recvfrom(1024)
    print(data.decode('UTF-8') + "received from"+ str(addr))
    # sock.sendto(("Hello "+ str(addr)).encode('UTF-8'),(host,port))