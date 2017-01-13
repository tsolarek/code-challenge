# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.
#
from HammingAnalysis import HammingAnalysis


def compute(a_dna_string, b_dna_string):
    hamming_analysis = HammingAnalysis(a_dna_string, b_dna_string)
    return hamming_analysis.hamming_distance
