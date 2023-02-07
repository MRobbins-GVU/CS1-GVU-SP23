# Rock Paper Scissors question

def check_turns(p1, p2):
    if (p1 == p2):
        print("Tie")
    elif (p1 == 1 and p2 == 2):
        print("Computer Wins")
    # TODO: you will need to check the remaining conditions
        
        
def main():
    
    # TODO: you will need to fill in how this while loop runs, instead of using while True
    # if you leave it as "while True", it will never end.
    while True:
        # TODO: you will need to fill in this randrange to make sure there is a chance to generate 1, 2, or 3
        computer = randrange()
        
        # TODO: you will need to ask the player to enter a value, and call the check_turns function
        player = int(input())
        
main()
