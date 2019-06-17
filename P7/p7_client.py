import http.client
import json
import requests
import sys
from seq import Seq

SERVER = "http://rest.ensembl.org"
ext = "/sequence/id/ENSG00000165879"
PORT = 80

r = requests.get(SERVER + ext, headers={"Content-Type": "application/json", "Accept": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

dict = r.json()

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))


sequence = dict['seq']
sequence = Seq(sequence)

len_seq = sequence.len()
print("Length of the sequence:" , len_seq)

t_bases = sequence.count("T")
print("Number of T bases:", t_bases)


count = sequence.count("A")
for base in "ACTG":
    perc = sequence.perc(base)
    print("The percentage of the base {} is {}%". format(base, perc))
    if sequence.count(base) >= count:
        count = sequence.count(base)
        mayor = base

perc_mayor = (count / len_seq) *100
print("The most popular base is: {}, with a {}%".format(mayor, perc_mayor))
