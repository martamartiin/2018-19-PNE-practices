class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        complementary_seq = ""
        dictionary_bases = {"A":"T", "C":"G", "G":"C", "T":"A"}
        for base_s in self.strbases:
            for base, complement in dictionary_bases.items():
                if base_s == base:
                    complementary_seq += complement
        complement = Seq(complementary_seq)
        return complement

    def reverse(self):
        reverse_seq = self.strbases[::-1]
        reverse = Seq(reverse_seq)
        return reverse

    def count(self, base):
        return (self.strbases).count(base)

    def perc(self, base):
        tl = len(self.strbases)
        counter = self.strbases.count(base)
        perc = round((100 * counter)/ tl,1)
        return perc


