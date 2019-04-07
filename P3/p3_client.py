#creating a client for testing the server
import socket



#configuration of the server
IP = "192.168.1.79"
PORT = 8080

msg = """ATACCTT\nlen\ncomplement\ncountA\npercA\ncountC"""


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conecting to the Server (IP, PORT)
s.connect((IP, PORT))

# Sending message to the server
s.send(str.encode(msg))
response = s.recv(2048).decode()
print(response)
s.close()
