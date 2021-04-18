import socket

from tracert_as.models.icmp_packet import IcmpPacket
from tracert_as.services.whois_tracer import WhoisTracer


class Traceroute:
    def __init__(self, host: str, max_hops=30, ttl=1):
        self._host = socket.gethostbyname(host)
        self._max_hops = max_hops
        self._ttl = ttl

    @staticmethod
    def _is_over(icmp: IcmpPacket) -> bool:
        if icmp.type == icmp.code == 0:
            return True
        return False

    def _create_sockets(self) -> (socket.socket, socket.socket):
        send_sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM,
                                  socket.IPPROTO_ICMP)
        send_sock.setsockopt(socket.SOL_IP,
                             socket.IP_TTL,
                             self._ttl)
        recv_sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_RAW,
                                  socket.IPPROTO_ICMP)
        recv_sock.settimeout(3)
        return send_sock, recv_sock

    def make_trace(self):
        while self._ttl <= self._max_hops:
            sender_sock, receiver_sock = self._create_sockets()
            icmp_pack = IcmpPacket(0, 0)
            sender_sock.sendto(bytes(icmp_pack), (self._host, 80))
            try:
                data, address = receiver_sock.recvfrom(1024)
            except socket.timeout:
                yield '*\n'
                self._ttl += 1
                continue
            trace_node = WhoisTracer.get_whois_data(address[0])
            yield trace_node
            received_icmp = IcmpPacket.from_bytes(data[20:])
            if self._is_over(received_icmp):
                sender_sock.close()
                receiver_sock.close()
                break
            self._ttl += 1
            sender_sock.close()
            receiver_sock.close()
