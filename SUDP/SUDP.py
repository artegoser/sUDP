import socket
class sUDPsocket():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.retimeout = 5
        self.timeout = None

    def bind(self, addres):
        self.sock.bind(addres)

    def recvfrom(self, bytes):
        msg , address = self.sock.recvfrom(bytes)
        self.sock.sendto(("ok").encode("utf-8"),address)
        return msg, address
    
    def recv(self, bytes):
        msg , address = self.sock.recvfrom(bytes)
        self.sock.sendto(("ok").encode("utf-8"),address)
        return msg

    def sendto(self, msg, address):
        self.sock.sendto(msg,address)
        self.sock.settimeout(self.retimeout)
        try:
            ok , addressok = self.sock.recvfrom(1024)
        except:
            return False
        finally:
            self.sock.settimeout(self.timeout)
        if ok.decode("utf-8") == "ok" and addressok == address:
            return True
        elif addressok != address:
            return "received a \"ok\" message from the wrong address"
        else:
            return False

    def settimeout(self, timeout):
        self.timeout = timeout
    
    def sendfile(self):
        pass
    
    def recvfile(self):
        pass
