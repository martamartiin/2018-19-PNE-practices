f = open("CPLX2.txt",'r')
c_a = 0
c_c = 0
c_g = 0
c_t = 0
for line in f:
    line = line.strip("\n")
    if line.startswith(">"):
        pass
    else:
        a = line.count("A")
        c = line.count("C")
        g = line.count("G")
        t = line.count("T")
        c_a += a
        c_c += c
        c_g += g
        c_t += t
print( "The number of times the different bases appear are:")
print("A:", c_a)
print("C:", c_c)
print("G:", c_g)
print("T:", c_t)
