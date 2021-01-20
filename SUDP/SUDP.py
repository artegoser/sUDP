import socket
class sUDPsocket():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    def bind(self, addres):
        self.sock.bind(addres)
    def recvfrom(self, bytes):
        msg , address = self.sock.recvfrom(bytes)
        self.sock.sendto(("ok").encode("utf-8"),address)
        return msg, address
    #def recv(self, bytes):
    #    pass
    def sendto(self, msg, address):
        self.sock.sendto(msg,address)
        ok , addressok = self.sock.recvfrom(bytes) #переделать в multithreading
        if ok.decode("utf-8") == "ok" and addressok == address:
            return True
        elif addressok != address:
            raise Exception("received a message from the wrong address")
        else:
            return False