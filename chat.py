import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_port = ("143.47.184.219", 5378)
sock.connect(host_port)

# Sometimes, the operating system cannot send everything immediately.
# For example, the sending buffer may be full.
# send returns the number of bytes that were sent.
# num_bytes_to_send = sock.send(string_bytes[bytes_len-num_bytes_to_send:])

sock.send("HELLO-FROM abbe\n".encode("utf-8"))

while True:
    data = sock.recv(4096).decode("utf-8").strip()

    print(data)

    if not data:
        break

sock.close()