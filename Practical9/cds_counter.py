# in my code, I considered the case of having multiple start codons and stop codons

# import regular expression package
# define the sequence we are interested in
# find all start codons and stop codons
# for each pair of start and stop codons,
#   if the index of end is after the index of start, we count once
# print out the count
import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
# find start and stop codons
starts = [i.start() for i in re.finditer('ATG', seq)]
ends = [i.start() for i in re.finditer('TAA|TAG|TGA', seq)]
count = 0
# count CDS
for start in starts:
    for end in ends:
        if end > start:
            count += 1
print(count)
