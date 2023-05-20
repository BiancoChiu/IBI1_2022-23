# in my code, I considered the case of having multiple start codons and stop codons

# ask the user to type in a stop codon
# create a new file to store genes ending with the specific stop codon
# read the fasta file
#   store each gene name and sequence
#   if the sequence ending with the specific stop codon
#       calculate the possible cds (I considered the case where the start codon is in the middle)
#       write the name, number of cds and sequence of the gene in the new file

import re
stop_codons = input('your input should be TAA, TAG or TGA: ')
new = open('%s_stop_gene.fa' % stop_codons, 'w')
with open(r'G:\test\IBI1_2022-23\Practical9\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as f:
    s = ''
    gene_name = ''
    for i in f:
        if i.startswith('>'):
            if s.endswith(stop_codons + '\n'):
                L = s.split()
                s = ''.join(L)
                starts = [j.start() for j in re.finditer('ATG', s)]
                ends = [j.start() for j in re.finditer(stop_codons, s)]
                count = 0
                for start in starts:
                    for end in ends:
                        if end > start:
                            count += 1
                new.write(gene_name + ' number of coding sequences: %s ' % count + '\n' + s + '\n')
            s = ''
            gene_name = i.split()[0]
            continue
        s += i
new.close()
