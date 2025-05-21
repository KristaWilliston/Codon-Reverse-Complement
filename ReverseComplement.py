# Write a Python program to compute the reverse complement of a codon
# Add the “complement” function of this lecture(slide 9) as provided.
# Modularize! Place the reverse complement code in a new function. 
# Call the new function with a variety of codons
# Change the complement function to handle upper and lower-case nucleotide
# symbols.
# Test the code with upper and lower-case codons.

# The input codon for the program
codon = 'ATG'
#codon = 'gta'
#codon = 'TcA'
#codon = 'ccc'

# Reverse Complement function
def reverseComplement(codon):
    first = codon[0]
    second = codon[1]
    third = codon[2]

    firstComplement = complement(first)
    secondComplement = complement(second)
    thirdComplement = complement(third)

    reversedCodon = thirdComplement + secondComplement + firstComplement

    return reversedCodon

# Determine the complementary nucleotide in uppercase and lowercase
def complement(nuc):
    if nuc == 'A':
        comp = 'T'
    elif nuc == 'T':
        comp = 'A'
    elif nuc == 'C':
        comp = 'G'
    elif nuc == 'G':
        comp = 'C'
    elif nuc == 'a':
        comp = 't'
    elif nuc == 't':
        comp = 'a'
    elif nuc == 'c':
        comp = 'g'
    elif nuc == 'g':
        comp = 'c'
    else:
        comp = nuc
    return comp

# Reverse Complement function
def reverseComplement(codon):
    first = codon[0]
    second = codon[1]
    third = codon[2]

    firstComplement = complement(first)
    secondComplement = complement(second)
    thirdComplement = complement(third)

    reversedCodon = thirdComplement + secondComplement + firstComplement

    return reversedCodon


print("The input codon:",codon)
print("The reverse complement:",reverseComplement(codon))
