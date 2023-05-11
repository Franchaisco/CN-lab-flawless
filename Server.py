import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    host_port = ("127.0.0.1", 4321)
    sock.bind(host_port)
    sock.listen(3000)
    data = sock.recv(4096).decode("utf-8").strip()
    
try:
    sock.send("how to handle errors?".encode("utf-8"))
    answer = sock.recv(4096)
except OSError as msg:
    print(msg)
