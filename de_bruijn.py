## Stand alone De Bruijn 
# This does not create a visualization. For graph visualization, refer to de_bruijn.ipynb 

# Inputs: 
    # File with sequence (ideally one created using random DNA generator) -- sys.argv[1]
        # Unsure of how this would perform with file that contains more than 1 DNA sequence 
    # kmer length -- sys.argv[2]
# Returns:
    # right-mers
    # left-mers
    # nodes
    # edges
    # Number of Kmers
    # Sequence Length of Input DNA 
    # Coverage Rate
    # Erorr Rate 

import sys

def make_kmers(sequence, kmer_size):
    """
    inputs: 
        sequence: dna sequence 
        kmer_size
    """
    kmer_list = []
    num_kmers = len(sequence) - kmer_size + 1

    for i in range(num_kmers):
        seqs = sequence[i:i + kmer_size]
        kmer_list.append(seqs)

    return kmer_list

def de_bruijn(kmer):
    # create empty dictionaries 
    left_mers=[] # left kmer, this will overlap with the right kmer
    right_mers=[] # right kmer, this will overlap with the left kmer
    edges = [] # edge, this corresponds to the overlap between two kmers (1 left kmer and 1 right kmer)
    nodes = set() # nodes will be the kmers

    # first, divide the kmer into left and right mers 
    for i in range(len(kmer)):
        divide = len(kmer[i])
        right_mers.append(kmer[i][1:divide])
        left_mers.append(kmer[i][0:divide-1])
    
    # create the edges and nodes 
    for j in range(len(kmer)):
        edges.append((left_mers[j], right_mers[j])) # creating edge where parts of the left and right mers overlap
        nodes.add(left_mers[j]) # combine the right and left mers
        nodes.add(right_mers[j])

    return right_mers, left_mers, nodes, edges

# make finalizing graph structure 
def main():
    sequence = sys.argv[1]
    with open(sequence) as file:
        next(file) # skips past the first line that says sequence 
        data = file.read()
    kmer_len = int(sys.argv[2])

    k=(make_kmers(sequence, kmer_len))
    right_mers, left_mers, nodes, edges = de_bruijn(k)

    print("Input Sequence:", data)
    print("Right-mers:", right_mers)
    print("Left-mers:", left_mers)
    print("Nodes:", nodes)
    print("Edges:", edges)
    print("Number of Kmers:", len(k))
    print("Kmer length:", kmer_len)
    print('Sequence length:', len(data))

    # coverage calculation
    # coverage = L*N/G 
    # L = length of kmer 
    # N = number of generated kmers 
    # G = total length of the input sequence 
    coverage = ((kmer_len*len(k))/len(data))
    print("Coverage:", coverage)

    # error rate calculation
    error_calc = (1-(1*10e-2))
    error_rate = len(data)*(error_calc)
    print('Error Rate per Base = 1-(1*10e-2)')
    print("Error Amount for This Sequence:", error_rate)
    
if __name__ == '__main__':
    main()