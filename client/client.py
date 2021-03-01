import socket

BUFFER = 1024


class Client:
    def __init__(self) -> None:
        self.sock = socket.socket()

    def connect(self, hostname: str, port: int):
        self.sock.connect((hostname, port))

    def send_text(self, text: str) -> str:
        self.sock.sendall(text.encode("utf-8"))
        chunk = self.sock.recv(BUFFER)
        if chunk:
            return chunk.decode("utf-8")
        return ""
