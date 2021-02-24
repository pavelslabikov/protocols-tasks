from client.client import Client


if __name__ == "__main__":
    client = Client("localhost", 21001)
    client.connect()