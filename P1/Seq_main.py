from Seq import Seq

seq1 = Seq("ACCTGTGACCA")
seq2 = Seq("GTCGTTACA")
seq3 = seq1.complement()
seq4 = seq3.reverse()

l_seq = [seq1, seq2, seq3, seq4]

for i, seq in enumerate(l_seq):
    print("Sequence:", seq.strbases)
    
    print("Length:{}".format(seq.len))
    
    print("Bases count: A:{}/n".format(seq.count('A')))
    print("C:{}/n".format(seq.count('C')))
    print("T:{}/n".format(seq.count('T')))
    print("G:{}/n".format(seq.count('G')))
    
    print("Bases percentage: A: {}%/n".format(seq.perc('A')))
    print("C: {}%/n".format(seq.perc('C')))
    print("T: {}%/n".format(seq.perc('T')))
    print("G: {}%/n".format(seq.perc('G')))
    
