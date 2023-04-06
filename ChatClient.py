import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_port = ("143.47.184.219", 5378)
sock.connect(host_port)

string_bytes = "Sockets are great!".encode("utf-8")
bytes_len = len(string_bytes)
num_bytes_to_send = bytes_len
while num_bytes_to_send > 0:
# Sometimes, the operating system cannot send everything immediately.
# For example, the sending buffer may be full.
# send returns the number of bytes that were sent.
num_bytes_to_send -= sock.send(string_bytes[bytes_len-num_bytes_to_send:])

client_name = input("Enter your name:")

string_bytes = client_name.encode("utf-8")
bytes_len = len(string_bytes)
num_bytes_to_send = bytes_len
while num_bytes_to_send > 0:
# Sometimes, the operating system cannot send everything immediately.
# For example, the sending buffer may be full.
# send returns the number of bytes that were sent.
num_bytes_to_send -= sock.send(string_bytes[bytes_len-num_bytes_to_send:])

def nameIsValid(name):
    pass



nameIsValid(client_name)
