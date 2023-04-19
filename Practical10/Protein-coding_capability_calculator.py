# the calculater function
#   find start codons and stop codons
#   calculate the percents of coding sequence
#   judge the percents with the standard
#   return the output
import re


def coding_calculator(seq):
    starts = [i.start() for i in re.finditer('ATG', seq)]
    ends = [i.start() for i in re.finditer('TGA', seq)]
    percents = ((ends[-1] + 3) - starts[0]) / len(seq)
    if percents > 0.5:
        return percents, 'protein-coding'
    elif percents / len(seq) < 0.1:
        return percents, 'non-coding'
    else:
        return percents, 'unclear'


# to show how to call the function, I assume the input sequence
sequence = 'aTGATCGACGATCGATCATCATCGATCGAactTCGATGCTACGTACGTAactgGCTATgaCG'
# when doing test, please uncomment the code in the next line
# sequence = input()
sequence = sequence.upper()
percentage, label = coding_calculator(sequence)
print('coding percentage: %.2f' % percentage, 'coding or not: %s' % label)
