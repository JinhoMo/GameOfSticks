#Level 1
print(f"{'*'*10}The Game of Sticks!!!{'*'*10}\nChoose to remove either 1, 2, or 3 sticks.\n")

sticks = 15
while True:
    print(f"{sticks} sticks are remaining.")
    remove = int(input("How many sticks would you like to remove?"))
    if sticks <= 3:
        if remove > sticks:
                 print(f"Illegal move! Only {sticks} {'stick is' if sticks == 1 else 'sticks are'} remaining.\n")
                 continue
   
    if remove == 1:
        sticks -= 1
    elif remove == 2:
        sticks -= 2
    elif remove == 3:
        sticks -= 3
    else:
        print("You are only able to remove 1 to 3 sticks. Please retry")

    if sticks == 0:
        print("No sticks are remaining. End the game. Thank you for playing.")
        break

    print()
