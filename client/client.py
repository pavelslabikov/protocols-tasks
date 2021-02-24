import socket


class Client:
    def __init__(self, hostname: str, port: int) -> None:
        self.sock = socket.socket()
        self.host = hostname
        self.port = port

    def connect(self):
        self.sock.connect((self.host, self.port))
        while True:
            self.sock.sendall(input("Enter text: ").encode("utf-8"))
            data = self.sock.recv(1024)
            print(data.decode())
