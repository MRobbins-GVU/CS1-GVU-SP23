
#TODO update this statement to import the function you need from random
from random import ?

def going(big, home):
    ''' Generate a random number to decide if you're going big, or you're going home. '''
    # TODO generate your first random integer
    
    # The easiest way to check if something is closer to two numbers, is to compare it to the midpoint.
    # If the number is greater than the midpoint, then it's closer to the bigger number. 
    # If the number is smaller than the midpoint, then it's closer to the smaller number.
    # HINT: read carefully - what does the problem say you should do if the number matches the midpoint?
    midpoint = (big + home) / 2
    
    # TODO: compare the random integer and the midpoint
    while ? :
        # TODO: keep track of the number of times the loop runs
        # TODO generate a new random integer 
        
    # TODO return the number of times the loop runs.
    return ?
    
def main():
    print(going(100, 1))
    print(going(5000, 5))
    
main()
