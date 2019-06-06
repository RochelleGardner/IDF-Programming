import socket

HOST = '127.0.0.1'
PORT = 65432

b = bytes

def get_host_ip(hostname, fallback=None):
    ip_addr = (hostname)
    if not ip_addr:
        try:
            ip_addr = socket.gethostbyname(hostname)
        except:
            print("Failed to resolve hostname '%s'" % (hostname))
            return fallback
    return ip_addr 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn,address = s.accept()
    hostname = socket.gethostname()
    addr = socket.gethostbyname(hostname)
    with hostname:
        while True:
            get_host_ip(hostname)
            continue
    print('Connection from: ', addr)
    print('Hostname: ', hostname)
    data = (hostname, addr)

    conn.sendall(data)
