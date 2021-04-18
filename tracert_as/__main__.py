import argparse

from tracert_as.services.route_tracer import Traceroute


def prepare_args():
    parser.add_argument('hostname', type=str, help="Hostname to trace")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    prepare_args()
    args = parser.parse_args()
    traceroute = Traceroute(args.hostname)
    trace_result = traceroute.make_trace()
    for count, el in enumerate(trace_result, start=1):
        print(f'{count}. {el}')
