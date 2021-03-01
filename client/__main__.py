from client.client import Client
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    client = Client()
    try:
        client.connect(args.host, args.port)
        while True:
            text = input("Enter text to send: ")
            response = client.send_text(text)
            print("Response: " + response)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        exit()
