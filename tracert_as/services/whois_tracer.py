import socket

from tracert_as.models.whois_record import WhoisRecord


class WhoisTracer:
    @staticmethod
    def get_whois_data(address: str) -> WhoisRecord:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((socket.gethostbyname('whois.iana.org'), 43))
        sock.send((address + '\r\n').encode('utf-8'))
        result_data = {}
        try:
            first_data = sock.recv(1024).decode()
            if 'refer' in first_data:
                refer_ind = first_data.index('refer')
                first_data = first_data[refer_ind:].split('\n')[0].replace(' ', '').split(':')
                whois_server = first_data[1]
                whois_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                whois_sock.connect((whois_server, 43))
                whois_sock.send((address + '\r\n').encode('utf-8'))
                data = b''
                current_part = whois_sock.recv(1024)
                while current_part != b'':
                    data += current_part
                    current_part = whois_sock.recv(1024)
                data = data.decode().lower()
                for el in ['country', 'origin', 'originas']:
                    if el in data:
                        ind = data.index(el)
                        record = data[ind:].split('\n')[0]
                        record = record.replace(' ', '').split(':')
                        result_data[record[0]] = record[1]
                return WhoisRecord(address, result_data)
        except socket.timeout:
            pass
        finally:
            sock.close()
            return WhoisRecord(address, result_data)
