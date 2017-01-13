class HammingAnalysis:
    def __init__(self, a_dna_string, b_dna_string):
        self.a_dna_string = a_dna_string
        self.b_dna_string = b_dna_string
        self.dna_string_length = self.__get_dna_string_length()
        self.hamming_distance = self.__calculate_hamming_distance()

    def __check_if_zero_length(self):
        if len(self.a_dna_string) == 0 and len(self.b_dna_string) == 0:
            return True
        else:
            return False

    def __get_dna_string_length(self):
        if len(self.a_dna_string) == len(self.b_dna_string):
            return len(self.a_dna_string)
        else:
            raise ValueError

    def __calculate_hamming_distance(self):
        hamming_distance = 0

        if self.__check_if_zero_length():
            return hamming_distance
        else:
            for nucleotide in range(0, self.dna_string_length):
                if self.a_dna_string[nucleotide] != self.b_dna_string[nucleotide]:
                    hamming_distance += 1
            return hamming_distance
