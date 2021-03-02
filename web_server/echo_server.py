import socket
import threading
import time

TIMEOUT = 15
BUFFER = 1024


class Server:
    def __init__(self, hostname: str, port: int) -> None:
        self.sock = socket.socket()
        self.host = hostname
        self.port = port

    def start_server(self) -> None:
        self.sock.bind((self.host, self.port))
        self.sock.listen()
        while True:
            conn, _ = self.sock.accept()
            print(f"Connected {_}")
            self.serve_client(conn)

    def serve_client(self, client_sock: socket.socket):
        client_sock.settimeout(TIMEOUT)
        while True:
            data = client_sock.recv(1024)
            if data == b"":
                client_sock.shutdown(1)
                client_sock.close()
                break
            if data:
                client_sock.sendall(data)
