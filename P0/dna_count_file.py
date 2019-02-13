f = open("dna.txt", 'r')
c_a = 0
c_c = 0
c_g = 0
c_t = 0
for line in f:
    line = line.strip("\n")
    a = line.count("A")
    c = line.count("C")
    g = line.count("G")
    t = line.count("T")
    c_a += a
    c_c += c
    c_g += g
    c_t += t

print("The number of times the dofferent bases appear are: \n A:", c_a, "\n G:", c_g,"\n T:", c_t, "\n C:", c_c )

