import socket
import threading


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
            client_thr = threading.Thread(target=self.serve_client, args=(conn,))
            client_thr.start()
            client_thr.join()

    def serve_client(self, client_sock: socket.socket):
        while True:
            data = client_sock.recv(4096)
            if data:
                client_sock.sendall(data)
