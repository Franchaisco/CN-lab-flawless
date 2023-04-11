import socket


host_port = ("143.47.184.219", 5378)


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



def userInput():
    while True:
        mes = input(" ")
        if mes.startswith("!quit"):
            sock.close()
            break
        elif mes.startswith("!who"):
            list_mes = "LIST\n"
            sock.send(list_mes.encode("utf-8")).
