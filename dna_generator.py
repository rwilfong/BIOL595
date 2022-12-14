# Standalone DNA Generator 
# Inputs from command line (in order): 
    # number of DNA sequences 
    # minimum length of sequence
    # max length of sequence
    # file name for output file 
# example:
    # python dna_generator.py 1 20 25 sequence.fa 


from random import randint
import textwrap as tw
import random
import sys 

# Generate DNA Sequences 
# DNA base randomizer
def dna_base(x):
    return {
        0: 'G',
        1: 'C',
        2: 'A',
        3: 'T'
    }[x]

# generate dna sequences 
def gen_dna(num_dna, min_length, max_length):
    dna_dict = { } # create empty dictionary 
    for i in range(num_dna):
        dna_sequence = ""
        for _ in range(random.randint(min_length, max_length)):
            dna_sequence += dna_base(random.randint(0,3))
        dna_title = ">sequence " + str(i + 1) # make it a FASTA format 
        dna_dict[dna_title] = dna_sequence

    return dna_dict

# function to write generate sequence to a file 
def write_sequence(dictionary, filePath):
    with open (filePath, "w") as f:
        for dna_key, dna_value in dictionary.items():
            f.write(dna_key)
            f.write('\n')
            f.write('\n'.join(tw.wrap(dna_value, 10000))) 
            #f.write('\n')

def main():
    dna_dict = gen_dna(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    write_sequence(dna_dict, sys.argv[4])

if __name__ == "__main__":
    main()