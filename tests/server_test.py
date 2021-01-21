import SUDP
import time

sock = SUDP.sUDPsocket()
sock.bind (('192.168.0.183',9090))

while True:
    msg , address = sock.recvfrom(1024)
    #time.sleep(3)
    sock.timeout = 1 #any timeout
    print(sock.sendto(("lol").encode("utf-8"), address))