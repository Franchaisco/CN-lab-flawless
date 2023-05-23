import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 5353
address = (host, port)

users = {}

def receive_client(conn, addr):
    print("New connection! " + str(addr) + " connected")
    
    connection = True
    while connection:
        try:
            mes = conn.recv(4096).decode("utf-8").strip()
            if not mes:
                print("Connection lost")
                conn.close()
                break
            elif mes.startswith("HELLO-FROM"):
                username = mes.split()[1]

                # check if username is already in users, if so send in-use
                if username in users:
                    # send in use
                    mes = "IN-USE"
                    conn.send(mes.encode("utf-8"))

                # otherwise add to users
                users[username] = conn

                mes = "HELLO " + username
                print("Incoming hello " + username)
                conn.send(mes.encode("utf-8"))
            elif mes.startswith("LIST"):
                list = ", ".join(users.keys())
                mes = "LIST-OK " + list
                conn.send(mes.encode("utf-8"))
            elif mes.startswith("SEND"):
                des_user = mes.split()[1]
                des_mes = mes.split(maxsplit=2)[2]
            
                if des_mes == '':
                    mes = "BAD-RQST-BODY\n"
                    conn.send(mes.encode("utf-8"))

    
                if des_user in users:
                    mes_user = "SEND-OK"
                    conn.send(mes_user.encode("utf-8")) 
                    mes = "DELIVERY\n " + username + " " + des_mes + "\n"
                    

                    des_conn = users[des_user]
                    des_conn.send(mes.encode("utf-8"))
                else:
                    mes = "BAD-DEST-USER\n"
                    conn.send(mes.encode("utf-8"))
            
            else:
                mes = "BAD-RQST-HDR\n"
                conn.send(mes.encode("utf-8"))       

        except KeyboardInterrupt:
            break
        except ConnectionResetError:
            break
    conn.close()

print("Initiate server...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(address)
sock.listen()
print("Listening on " + host + ": " + str(port))

while True:
    try:
        conn, addr = sock.accept()
        thr = threading.Thread(target=receive_client, args=(conn, addr))
        thr.daemon = True
        thr.start()
    except KeyboardInterrupt:
        break
