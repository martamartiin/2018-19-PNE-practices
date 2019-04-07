#client that sends a dna sequence to a server

from Seq import Seq
import socket

#making a loop
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #server´s configuration
    PORT = 8080
    IP = "192.168.1.79"
    
    # Connecting to the server
    s.connect((IP, PORT))
    
    #Converting the sequence into class ´Seq'
    sequence = Seq(input("Enter the sequence: "))
    
    # receive the complement and the reverse of the sequence
    comp_seq = sequence.complement()
    rev_seq = sequence.reverse()
    
    # Convert to sequence (string)
    complement_s = comp_seq.strbases
    reverse_s = rev_seq.strbases
    
    # Sending the message to the server
    s.send(str.encode("The complement sequence is: "))
    s.send(str.encode(complement_s))
    s.send(str.encode("\nThe reverse sequence is: "))
    s.send(str.encode(reverse_s))
    s.close()
