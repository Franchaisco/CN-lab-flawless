import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    host_port = ("127.0.0.1", 4321)
    sock.connect(host_port)
    sock.listen(3000)
    data = sock.recv(4096).decode("utf-8").strip()
    hello_msg = "HELLO-FROM"
    hello = hello_msg + " "
    if data.startswith(hello_msg)
        username = hello[10:]
        sock.send("HELLO " + username).encode("utf-8")