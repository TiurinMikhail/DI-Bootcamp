#TIC TAC Example

VALID_MOVES = [i for i in range(1,10)]

while True:
    try:
        move = int(input("Enter your number:__"))
        if move not in VALID_MOVES:
            raise ValueError()
        break
    except ValueError as e:
        print(e)
        print("Invalid input. Please add a number from 1 - 9")
    finally:
        print("Thank you for using correct input!")

print(move)

