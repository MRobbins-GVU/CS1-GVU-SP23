

def feels_even(items):
    #TODO Fill in the blanks with the needed values
    for ? in ? :
        #TODO: remember that to check if a value is even, you check if val % 2 == 0
        #Hint: You may need to change == to !=, depending on your implementation
        if ? % 2 == 0:
            ?
            
        #TODO: to check if a value is divisible by 5, you can check value % 5 == 0 
        #Hint: You may also need to change == to !=, depending on your implementation
        else if ? % 5 == 0:
            ?
            
    #Hint: You may also need to change to return False, depending on your implementation
    return True
    
 
def main():
    test1 = [2, 0, 14, 8, 5, 15]            # True
    print(feels_even(test1))
    
    test2 = [8, 30, 9, 10, 4, 5, 2, 12]     # False
    print(feels_even(test2))
    
    
main()
