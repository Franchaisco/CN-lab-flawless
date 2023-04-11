import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_port = ("143.47.184.219", 5378)
sock.connect(host_port)
username = input("Enter valid username:")
message = 
sock.send("HELLO-FROM \n".encode("utf-8"))

while True:
    data = sock.recv(4096).decode("utf-8").strip()

    print(data)
    sock.close()

    if not data:
        break

sock.close()

