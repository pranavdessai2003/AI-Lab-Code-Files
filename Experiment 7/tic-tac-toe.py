import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def evaluate(board):
    # Check rows
    for row in board:
        if row.count("X") == 3:
            return 10
        elif row.count("O") == 3:
            return -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == "X":
                return 10
            elif board[0][col] == "O":
                return -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return 10
        elif board[0][0] == "O":
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return 10
        elif board[0][2] == "O":
            return -10

    # If no winner
    return 0

def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def minimax(board, depth, is_maximizer):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_maximizer:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, not is_maximizer))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, not is_maximizer))
                    board[i][j] = " "
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while is_moves_left(board):
        print_board(board)
        move = input("Enter your move (row column): ").split()
        row, col = int(move[0]), int(move[1])
        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        board[row][col] = "O"

        if evaluate(board) == -10:
            print_board(board)
            print("You win!")
            return

        if not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            return

        print("Computer is making its move...")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = "X"

        if evaluate(board) == 10:
            print_board(board)
            print("Computer wins!")
            return

        if not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            return

if __name__ == "__main__":
    play_game()
