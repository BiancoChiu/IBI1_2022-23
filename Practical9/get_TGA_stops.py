# create a new file to store genes ending with TGA
# read the fasta file
#   store each gene name and sequence
#   if the sequence ending with TGA
#       write the name and sequence of the gene in the new file

genes = open(r'G:\test\IBI1_2022-23\Practical9\TGA_genes.fa', 'w')
with open(r'G:\test\IBI1_2022-23\Practical9\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as f:
    s = ''
    for i in f:
        if i.startswith('>'):
            if s.endswith('TGA\n'):
                genes.write(gene_name + '\n' + s)
            s = ''
            gene_name = i.split()[0]
            continue
        s += i
genes.close()
