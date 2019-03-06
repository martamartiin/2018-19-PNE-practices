from Seq import Seq

seq1 = Seq("ACCTGTGACCA")
seq2 = Seq("GTCGTTACA")
seq3 = seq1.complement()
seq4 = seq3.reverse()

l_seq = [seq1, seq2, seq3, seq4]

for i, seq in enumerate(l_seq):
    print("Sequence:", seq.strbases)
    print("Length:{}".format(seq.len))
    print("Bases count: A: {} C:{} G:{} T: {}".format(seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')))
    print("Bases percentage: A: {}% C:{}% G:{}% T:{}%".format(seq.perc('A'), seq.perc('C'), seq.perc('G'),
                                                              seq.perc('T')))



