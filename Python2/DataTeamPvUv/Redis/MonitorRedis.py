#!/usr/bin/env python
import sys
import os
import socket

try:
    port = sys.argv[2]
except IndexError:
    port = 6379

key_dick = {}


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        (addr, port) = s.getsockname()
        s.close()
    finally:
        s.close()
    return addr


def get_curr_connections():
    return float(key_dick['connected_clients'])


def get_qps():
    return float(key_dick['total_commands_processed'])


def get_mem_fragmentation_ratio():
    return float(key_dick['mem_fragmentation_ratio'])


def get_usage():
    return float(key_dick['used_memory'])
    return usage


if __name__ == '__main__':
    local_ip = get_local_ip()
    cmd = '/Data/app_1/redis/src/redis-cli -h ' + local_ip + ' -p ' + str(port) + ' info'
    for i in os.popen(cmd):
        key = i.split(':')[0].strip()
        value = i.split(':')[1].strip()
        key_dick[key] = value
    status_data_array = {
        'usage': 'get_usage()',
        'curr_connections': 'get_curr_connections()',
        'qps': 'get_qps()',
        'mem_fragmentation_ratio': 'get_mem_fragmentation_ratio()'
    }
    print"%.2f" % eval(status_data_array[sys.argv[1]])
