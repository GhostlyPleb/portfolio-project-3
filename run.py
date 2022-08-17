from random import randint

board = []

for x in range(0, 5):
    board.append(["0"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("  *** LETS PLAY BATTLESHIP!! ***    ")
print("You have 5 shots to hit the target! ")
print("  5 shots, 1 Target. YOU GOT THIS!  ")
print("Select row/column number between 0-4\n")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(6):
    print("\n")
    print("Turn", turn + 1)

    guess_row = int(input("Row Selection: "))
    guess_col = int(input("Column Selection: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("WELL DONE!! YOU SUNK MY BATTLESHIP!! I HOPE YOU'RE HAPPY NOW...\n")
        break

    elif turn == 4:
            print("YOU MISSED ALL YOUR SHOTS!")
            print("GAME OVER!!\n")
            break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.\n")
            print_board(board)

        elif (board[guess_row][guess_col] == "X"):
            print("SHOOTING AT THE SAME SPOT WON'T GET YOU ANYWHERE...\n")
            print_board(board)
        else:
            print("YOU MISSED!! (Not very good at this are we?)\n")
            board[guess_row][guess_col] = "X"
            print_board(board)