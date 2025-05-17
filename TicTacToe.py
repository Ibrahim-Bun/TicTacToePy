# create board layout

board = [" " for _ in range(9)]

# printing board with function

def print_board():
    for i in range(3):
        print(board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2])
        if i < 2:
            print("--+---+--")
#checking for winner

def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8], #rows
        [0,3,6],[1,4,7],[2,5,8], #collumns
        [0,4,8],[2,4,6]          #diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

#check for draw

def is_draw():
    return " " not in board

#handling player moves

def make_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, make a move (1-9): ")) -1
            if board[move] == " ":
                board[move] = player
                break
            else:
                print("Spot taken")
        except (ValueError, IndexError):
            print("Please enter a valid number between 1 and 9")

def main():
    current_player = "X"
    while True:
        print_board()
        make_move(current_player)
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if is_draw():
            print_board()
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

main()