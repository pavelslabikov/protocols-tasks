import argparse
from tracert_as.tracer import Tracer


def prepare_args():
    parser.add_argument("-t", "--ttl", type=int, metavar="SEC", help="Время жизни пакета", default=15)
    parser.add_argument("ip_address", type=str, help="IP адрес")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    prepare_args()
    args = parser.parse_args()
    tracer = Tracer()
    try:
        tracer.trace_address(args.ip, args.ttl)
    except Exception as e:
        print(e)
