import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board):
    """Displays the current state of the Tic Tac Toe board."""
    clear_screen()
    print("   0   1   2")
    print("0: " + " | ".join(board[0]))
    print("  " + "-"*11)
    print("1: " + " | ".join(board[1]))
    print("  " + "-"*11)
    print("2: " + " | ".join(board[2]))

def get_move(player):
    """Prompts the player for their move and returns the corresponding row and column."""
    while True:
        try:
            move = input(f"{player}'s turn. Enter row and column (e.g. '0 2'): ").split()
            row, col = int(move[0]), int(move[1])
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid move. Please enter a row and column between 0 and 2.")
        except:
            print("Invalid input. Please enter a row and column between 0 and 2.")

def check_winner(board):
    """Checks if the game has been won and returns the winner's symbol (X or O), or None if there is no winner."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    # No winner
    return None

def check_draw(board):
    """Checks if the game is a draw."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play_game():
    """Plays a game of Tic Tac Toe."""
    board = [[' ']*3 for _ in range(3)]
    current_player = 'X'
    winner = None
    while winner is None:
        display_board(board)
        move = get_move(current_player)
        row, col = move
        if board[row][col] != ' ':
            print("That space is already occupied. Please choose another one.")
        else:
            board[row][col] = current_player
            winner = check_winner(board)
            if winner is None:
                if check_draw(board):
                    print("The game is a draw!")
                    break
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                display_board(board)
                print(f"{winner} wins!")
                
if __name__ == "__main__":
    play_game()
