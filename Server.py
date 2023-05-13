import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 5353
address = (host, port)

def receive_client(conn, addr):
    print("New connection! " + str(addr) + " connected")
    
    connection = True
    while connection:
        mes = conn.recv(4096).decode("utf-8").strip()
        if mes == "!quit":
            mes = "You've disconnected from the server"
            sock.send(mes.encode("utf-8"))
            connection = False
        elif mes.startswith("HELLO_FROM"):
            mes = "HELLO " + str(addr)
            sock.send(mes.encode("utf-8"))
        elif mes.startswith("LIST"):
            
        elif mes.startswith("SEND"):
            print("SEND-OK")
        conn.close()





print("Initiate server...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(address)
sock.listen()
print("Listening on " + host + ": " + str(port))

while True:
    conn, addr = sock.accept()
    thr = threading.Thread(target=receive_client, args=(conn, addr))
    thr.start()
