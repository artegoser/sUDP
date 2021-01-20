import socket
class sUDPsocket():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    def bind(self, addres):
        self.sock.bind(addres)
    def recvfrom(self, bytes):
        msg , address = self.sock.recvfrom(bytes)
        if msg.decode("utf-8") == "ok":
            return
        self.sock.sendto(("ok").encode("utf-8"),address)
        return msg, address
    #def recv(self, bytes):
    #    pass
    def sendto(self, msg):
        pass