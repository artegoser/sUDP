import SUDP

server = '192.168.0.183', 9090 
sock = SUDP.sUDPsocket()

while True:
    print(sock.sendto(("lal").encode("utf-8"), server))
    sock.retimeout = 1 #any timeout
    msg , addres = sock.recvfrom(1024)