import socket

IP = "192.168.1.79"
PORT = 8080
MAX_OPEN_REQUESTS = 5


def process_client(cs):

    msg = cs.recv(2048).decode("utf-8")

    if msg == "192.168.1.79:8080":
        f = open("index.html")
        content = f.read()
        f.close()

    elif msg == "192.168.1.79:8080/Blue":
        f = open("blue.html")
        content = f.read()
        f.close()

    elif msg == "192.168.1.79:8080/Pink":
        f = open("pink.html")
        content = f.read()
        f.close()

    else:
        f = open("error.html")
        content = f.read()
        f.close()

    status_line = "HTTP/1.1 200 OK\r\n"
    header = "Content-type: text/html\r\n"
    header += "Content-length: {}\r\n".format(len(str.encode(content)))

    #Now we send the response
    response_msg = status_line + header + "\r\n" + content
    cs.send(str.encode(response_msg))

    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)