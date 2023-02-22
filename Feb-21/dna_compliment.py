# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:00:14 2023

@author: mrobbins
"""
# DNA Notes:
# A T C G
# T A G C

# Goal:
# Give:    ACTT
# Receive: TGAA

def compliment(base):
    ''' Given a single base, return its 
    complementary base '''
    if base == "A":
        return "T"
    if base == "T":
        return "A"
    if base == "C":
        return "G"
    if base == "G":
        return "C"
    
def dna_comp(dna_string):
    ''' Given a DNA string, return the 
    complement of the entire string '''
    
    comp_result = ""
    
    # First, go through every letter in dna_string
    for i in range(len(dna_string)):
        # For each letter, get the compliment
        letter = dna_string[i]
        comp_letter = compliment(letter)
        
        # Add that compliment to our growing result
        comp_result += comp_letter
        
    # Return the result
    return comp_result


def main():
    dna = "ACTT"
    print(dna_comp(dna)) # TGAA 
    
    # Test compliment function
    # print(compliment("A")) # T
    # print(compliment("T")) # A
    # print(compliment("C")) # G
    # print(compliment("G")) # C
    
main()
    







