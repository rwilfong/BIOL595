# De Bruijn Graph 

*Files:* 
- **de_bruijn.ipynb** -- this is a one stop shop. Generates random DNA sequence and then creates a De Bruijn graph and visualizes it using Toyplot. Inputs are dna sequence number (how many DNA sequences to make), minimum DNA length, maximum DNA length, file name (to write DNA sequence to), and kmer length. 

- **dna_generator.py** - standalone random DNA sequence generator. Inputs are number of DNA sequences, minimum sequence length, maximum sequence length, file name for output.

   Example: ```python dna_generator.py 1 10 20 sequence1.fa```


- **de_bruijn.py** - this is a standalone De Bruijn python script. Inputs are FASTA file with DNA sequence and kmer length. Order must be the sequence and kmer length. 
   
     Example: ```python de_bruijn.py sequence1.fa 4```


*Method:*

**DNA Sequence and Base Generator:** Creating a random DNA sequence generator that creates a random sequence based on the input length and number of sequences.
- Disclaimer: have not tried with multiple sequences written to the same file, unsure if this works for the De Bruijn graph. 

**Kmer Creator:** Takes the input DNA sequence and splits it into kmers based on the kmer length described by user. 

**De Bruijn Graph:** Takes the kmers created from the DNA sequence and splits them as right and left mers. These are then loaded into the nodes and edges. 


Library requirements: 
1. Toyplot 

   ```pip install toyplot```
   
2. Random 
    
    ```pip install random```
  
3. Textwrap 
    
    ```pip install textwrap```
  
4. NumPy 

      ```pip install numpy```
