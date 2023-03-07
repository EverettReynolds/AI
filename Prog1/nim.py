#!/usr/bin/python3

def playGame(piles):
    
    print("Here are The Number of Chips in the Piles Initially")
    print(piles)

    answer = int(input("Do you want you or the bot to go first? Enter 0 for Bot or Enter 1 for You. "))
    if(answer == 0):
        while True:
            print("Bot")
    elif(answer == 1):
        while True:
            print("Player")
            print(piles)
            userMove(piles)
            if winCheck(piles):
                print("You Win!")
                break
    else:
        print("Invalid Input. Enter Either 0 or 1.")
        playGame(piles)
  
    
     #while(True):

def userMove(piles):
    #print(piles)
    pile = input("Which Pile Would You Like to Take From?\n [A,B,C]? ")
    if pile == 'A':
        pile = 0
    if pile == 'B':
        pile = 1
    if pile == 'C':
        pile = 2
    #if  piles[pile] == 0:
        #print(" There are Zero Coins in This Pile. Choose Another.")
    while True:
        newVal = int(input("How Many Coins Do You Want to Take From This Pile? "))
        if newVal > piles[pile]:
            print("Try Again. Not Enough Coins in Pile. ")
            userMove(piles)
        else:
            piles[pile] = piles[pile] - newVal
        break



def compMove():
    print()
    #aaaaaah

def winCheck(piles):
    for i in range(len(piles)):
        if piles[i] != 0:
            return False
    return True


def makeAMove(stackNum,taken):
    try:
        if stacks[stackNum] - taken < 0:
            raise ValueError
        else:
            stacks[stackNum] = stacks[stackNum] - taken
    except ValueError as err:
        print(" There are not enough chips in the stack to make this move.")
        makeAMove( userMove() )
#def main()


piles = []
print("Welcome to NIM!")
piles.extend( list( map( int,input( "Enter a Positive Number of Chips for Piles A B C: " ).split() ) ) )
playGame(piles)



 