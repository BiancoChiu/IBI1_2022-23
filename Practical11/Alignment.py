# use the blosum package to access blosum62 matrix
# use itertools to combine three sequences
import blosum as bl
from itertools import combinations
matrix = bl.BLOSUM(62)
d = dict()
# open three files to read sequences
#   skip the first line, only read the second line
#   store the sequence in the dict
with open('ACE2_cat.fa', 'r') as f:
    n = 0
    for line in f:
        n += 1
        if n == 2:
            d['cat'] = line[: -1]
with open('ACE2_human.fa', 'r') as f:
    n = 0
    for line in f:
        n += 1
        if n == 2:
            d['human'] = line[: -1]
with open('ACE2_mouse.fa', 'r') as f:
    n = 0
    for line in f:
        n += 1
        if n == 2:
            d['mouse'] = line[: -1]
# combine the three sequences
L = ['cat', 'human', 'mouse']
combine = combinations(L, 2)


# define a function
#   use blosum62 matrix to get score for each letter
#   calculate the total score
#   return the score
def alignment(seq1, seq2):
    score = 0
    count = 0
    for i in range(len(seq1)):
        score += matrix[seq1[i]][seq2[i]]
        if seq1[i] == seq2[i]:
            count += 1
    percents = count / len(seq1)
    return score, percents


# use the function to calculate each pair of sequences, and print the result
for a, b in combine:
    print('Score and similarity of', a, 'and', b + ':', alignment(d[a], d[b]))
# Output:
# Score and similarity of cat and human: (3717.0, 0.8521739130434782)
# Score and similarity of cat and mouse: (3592.0, 0.8173913043478261)
# Score and similarity of human and mouse: (3579.0, 0.8211180124223603)

# The sequences of cat and human are most closely related
# cat&mouse and human&mouse sequences exhibit a slightly lower level of similarity
# The higher similarity between cat and human sequences could be attributed to a closer evolutionary relationship
