import random

while True:
    choice = input("Want to roll the die? (Y/N): ").lower()

    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"{die1}, {die2}")

    elif choice == 'n':
        print("Okay, exiting...")
        break

    else:
        print("Invalid choice dude! Enter Y or N.")
