import socket
import threading

host_port = ("192.168.56.1", 5353)


while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(host_port)
    username = input("Enter valid Username: ")
    username_mes = "HELLO-FROM " + username + "\n"
    sock.send(username_mes.encode("utf-8"))
    data = sock.recv(4096).decode("utf-8").strip()

    if data.startswith("HELLO"):
        print ("Hello " + username)
        break
    else:
        if data.startswith("IN-USE"):
            print("Username already taken. Try again.")
            sock.close()
        elif data.startswith("BUSY"):
            print("Server overloaded. Try again later.")
            sock.close()

def userRecv():
    while True:
        try:
            input_mss = sock.recv(4096).decode("utf-8").strip()
        except OSError:
            break
        
        if input_mss.startswith("LIST-OK"):
           userlist = input_mss.split(maxsplit=1)[1]
           print(userlist)
        elif input_mss.startswith("SEND-OK"):
            print("message sent to " + des_user)
        elif input_mss.startswith("BAD-DEST-USER"):
            print(des_user + " is not online")
        elif input_mss.startswith("DELIVERY"):
            splitted = input_mss.split(maxsplit=2)
            if len(splitted) != 3:
                print("Invalid message format")
            user = splitted[1]
            message = splitted[2]
            print(user + ": "+ message)
        elif input_mss.startswith("BAD-RQST-HDR"):
            print("bad header")
        elif input_mss.startswith("BAD-RQST-BODY"):
            print("Bad body")


           

receiveThread = threading.Thread(target=userRecv, daemon=True)
receiveThread.start()

def userInput():
    global des_user

    while True:
        mes = input("")
        if mes.startswith("!quit"):
            sock.close()
            break
        elif mes.startswith("!who"):
            list_mes = "LIST\n"
            sock.send(list_mes.encode("utf-8"))
        elif mes.startswith("@"):
            des_user = mes.split()[0][1:]
            des_mes = mes.split(maxsplit=1)[1]
            send_mes = "SEND " + des_user + " " + des_mes + "\n"
            sock.send(send_mes.encode("utf-8"))
        else:
            print("invalid comment")


userInput()
receiveThread.join()
