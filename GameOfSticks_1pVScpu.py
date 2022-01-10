#level 3
import random

def changePlayer():
    global nextMove
    nextMove += 1
    modifyMoves()

def modifyMoves():
    global nextMove
    global users
    if nextMove > len(users) - 1:
        nextMove = 0

def aiMove():
    global sticks
    aiCal = sticks - 1
    if sticks == 1:
        return 1
    if not aiCal % 4 == 0:
        return aiCal % 4
    return random.randint(1, 3)

print(f"{'*'*10}The Player VS Al Game of Sticks!!!{'*'*10}\nIn the game chose 1 to 3 sticks to remove on each term.")
users = ("Player", "AI")
sticks = 0
lastMove = 0
nextMove = 0

while True:
    try:
        user = int(input("Chose the number of sticks to play the game with: "))
        sticks = user
        break
    except ValueError:
        print("please Enter A Number")

print("Chose who goes first. Player or AI?")
while True:
    user = input("")
    if user.lower() == "player":
        nextMove = 0
        print("Player goes first")
    elif user.lower() == "ai":
        nextMove = 1
        print("AI goes first")
    else:
        print('Please input only player or AI')
        continue
    break

move = 0
while True:
    print(f"{sticks} sticks are remaining.")
    if users[nextMove] == "AI":
        remove = aiMove()
        print(f"AI decide to remove {remove} {'stick' if remove == 1 else 'sticks'}")
    else:
        try:
            remove = int(input(f"{users[nextMove]}, How many sticks would you like to remove?"))
        except Exception:
            print("Invalid move")
            continue
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
        print(f"\nNo sticks are remaining.\n\n{'Congrats!' if users[nextMove] == 'Player' else 'Too Bad XD.'} {users[nextMove]} is the winner!!\nEnd the game. Thank you for playing.")
        break

    print()
