#Level 2

def changePlayer():
    global nextMove
    nextMove += 1
    modifyMoves()

def modifyMoves():
    global nextMove
    global user
    if nextMove > len(user) - 1:
        nextMove = 0

print(f"{'*'*10}The 2P Game of Sticks!!!{'*'*10}\nChoose to remove either 1, 2, or 3 sticks.\n")
user = ["Player1", "Player2"]
sticks = 15
lastMove = 0
nextMove = 0

sub_user = []
for i in user:
    print(f"Please input the username for {i}")
    user = input()
    sub_user.append(user)
    
user = sub_user.copy()

while True:
    print(f"{sticks} sticks are remaining.")
    remove = int(input(f"{user[nextMove]}, How many sticks would you like to remove?"))
    if sticks <= 3:
        if remove > sticks:
                 print(f"Illegal move! Only {sticks} {'stick is' if sticks == 1 else 'sticks are'} remaining.\n")
                 continue
   
    if remove == 1:
        sticks -= 1
        lastMove = nextMove
        changePlayer()
    elif remove == 2:
        sticks -= 2
        lastMove = nextMove
        changePlayer()
    elif remove == 3:
        sticks -= 3
        lastMove = nextMove
        changePlayer()
    else:
        print("You are only able to remove 1 to 3 sticks. Please retry")


    if sticks == 0:
        print(f"No sticks are remaining.\n\nCongrats! {user[nextMove]} is the winner!!\nEnd the game. Thank you for playing.")
        break

    print()
