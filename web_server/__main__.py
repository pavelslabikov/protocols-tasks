import argparse

from web_server.echo_server import Server

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    server = Server(args.host, args.port)
    try:
        print(f"Starting server with address {args.host, args.port}")
        server.start_server()
    except KeyboardInterrupt:
        pass
    finally:
        exit()
