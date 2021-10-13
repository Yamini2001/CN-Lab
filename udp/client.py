import socket 
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = "127.0.0.1"
port = 9999
sock.sendto(("Hello "+ host).encode('UTF-8'),(host,port))