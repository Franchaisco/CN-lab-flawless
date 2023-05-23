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
                user_dic = str(users.keys())
                conn.send(mes.encode("utf-8"))
            elif mes.startswith("LIST"):
                list = user_dic[9:]
                mes = "LIST-OK " + list
                conn.send(mes.encode("utf-8"))
            elif mes.startswith("SEND"):
                des_user = mes.split()[1]
                des_mes = mes.split(maxsplit=1)[2]
                #print(des_user)
                #"""
                if des_user in users:
                    mes_user = "SEND-OK"
                    conn.send(mes_user.encode("utf-8")) 
                    conn = des_user
                    mes = "DELIVERY" + username + ": " + des_mes
                    conn.send(mes.encode("utf-8"))
                mes = "BAD-DEST-USER"
                conn.send(mes.encode("utf-8"))
                #"""
                    

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
        thr.start()
    except KeyboardInterrupt:
        break
