import os
import random
import time

# Function to draw the tic-tac-toe board
def draw_board(board: list[str]) -> None:
    """
    Function to draw the tic-tac-toe board.

    Arguments:
    - board (list): List representing the tic-tac-toe board.
    """
    # os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    # TODO: Draw the board. PRO TIP: look at the example `tictactoe.310.py
    print(f" {board[0]} | {board[1]} | {board[2]} \t1|2|3")
    print("---|---|--- \t-----")
    print(f" {board[3]} | {board[4]} | {board[5]} \t4|5|6")
    print("---|---|--- \t-----")
    print(f" {board[6]} | {board[7]} | {board[8]} \t7|8|9")
    print()

def draw_board_antonio(board):
    """
    Function to draw the tic-tac-toe board.

    Arguments:
    - board (list): List representing the tic-tac-toe board.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print("Tic-Tac-Toe\n")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} \t|1|2|3".format(board[3], board[4], board[5]))
    print("___|___|___\t------")
    print("   |   |    \t|4|5|6")
    print(" {} | {} | {} \t------".format(board[6], board[7], board[8]))
    print("   |   |   \t|7|8|9\n")


def check_win(board: list[str], player: str) -> bool:
    """
    Function to check if a player has won.
    A player wins if they have 3 consecutive marks in a row, column or diagonal.

    Arguments:
    - board (list): List representing the tic-tac-toe board.
    - player (str): Player's mark ('X' or 'O').

    Returns:
    - win (bool): True if the player has won, False otherwise.
    """
    # win_cond = [
    #   [board[0], board[1], board[2]],
    #   [board[3], board[4], board[5]],
    #   [board[6], board[7], board[8]],
    #   [board[0], board[3], board[6]],
    #   [board[1], board[4], board[7]],
    #   [board[2], board[5], board[8]],
    #   [board[0], board[4], board[8]],
    #   [board[2], board[4], board[6]],
    # ]

    # return [player] * 3 in win_cond

    win_cond = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ]

    for wc in win_cond:
        if board[wc[0]] == board[wc[1]] == board[wc[2]] == player:
            return True
    return False
        

# Function to play the game
def play_game():
    # The board variable store the state of the game, where board[0] is the top left corner and board[8] is the bottom right corner
    b = [' '] * 9
    # current_player = "X" if random.uniform(0, 1) > 0.5 else "O"
    current_player = random.choice(["X", "O"])
    # the game_over variable is used to know if the game is running or not
    game_over = False

    while not game_over:
        draw_board(b)

        move = int(input(f"Player {current_player}: Enter your move (1-9): "))

        # move_valid = False
        # while(move_valid == False):
        #     move = int(input(f"Player {current_player}: Enter your move (1-9): "))
        #     if 1 <= move <= 9 and b[move-1] == " ":
        #         b[move-1] = current_player
        #         move_valid = True
        #     else:
        #         print("Invalid move. Try again!")
        if not (1 <= move <= 9 and b[move-1] == " "):
        # if not (move in range(1, 10) and b[move-1] == " "):
            print("Invalid move. Try again!")
            time.sleep(0.3)
            continue
        
        b[move-1] = current_player
        
        if check_win(b, current_player):
            draw_board(b)
            game_over = True
            print(f"{current_player} won!")
        elif " " not in b:
            draw_board(b)
            game_over = True
            print("It's tie!") 
        else:
            current_player = "X" if current_player == "O" else "O"
# Start the game
play_game()
