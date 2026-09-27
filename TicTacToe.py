#TicTacToe.py Program

def print_board(board):
    """Prints the current state of the game board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    """Checks if the given player has won the game."""
    # Define all 8 possible winning combinations (rows, columns, diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    """Returns True if all positions are taken, False otherwise."""
    return all(space in ['x', 'o'] for space in board)

def play_game():
    """Main function to run the Tic-Tac-Toe game loop."""
    # Initialize the board with numbers 1-9 so players know how to pick a spot
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Get player input and validate it
        try:
            choice = int(input(f"Player {current_player}, choose a spot (1-9): ")) - 1
            if choice < 0 or choice > 8:
                print("Invalid input. Please choose a number between 1 and 9.")
                continue
            if board[choice] in ['X', 'O']:
                print("That spot is already taken! Try another one.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
            
        # Place the player's symbol on the board
        board[choice] = current_player
        print_board(board)
        
        # Check for a win
        if check_winner(board, current_player):
            print(f"🎉 Congratulations! Player {current_player} wins! 🎉")
            break
            
        # Check for a tie
        if is_board_full(board):
            print("🤝 It's a draw! Well played both.")
            break
            
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()