# initialize the board
board = ['' for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(f"{board[3*i]}  |  {board[3*i+1]}  |  {board[3*i+2]}  ")
        if i < 2:
            print("---|---|---")
            print()

            def check_winner(player):
                win_positions = [
                    [0,1,2],[3,4,5],[6,7,8],
                    #rows
                    [0,3,6],[1,4,7],[2,5,8],
                    #columns
                    [0,4,8],[2,4,6]
                    #diagonals
                ]
                for pos in win_positions:
                    if all(board[i] == player for i in pos):
                        return True
                    return False
                def is_draw():
                    return ' ' not in board
                #main game loop
                current_player ='X'

                while True:
                    print_board()
                    move = input(f"Player {current_player},choose a position (1-9):")

                    if not move.isdigit() or int(move) < 1 or int(move) > 9:
                        print("Invalid input.Try again.")
                        continue

                    index = int(move) - 1
                    if board[index] != '':
                        print("That spot is taken. Try again.")
                        continue
                    
                    board[index] = current_player

                    if check_winner(current_player):
                        print_board()
                        print(f"Player {current_player} wins!")
                        break
                    if is_draw():
                        print_board()
                        print("It's a draw!")
                        break
                    #switch players
                    current_player ='0'if current_player == 'X' else 'X'
