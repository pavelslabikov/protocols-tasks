from web_server.echo_server import Server

if __name__ == "__main__":
    server = Server("localhost", 21001)
    server.start_server()
    exit()
