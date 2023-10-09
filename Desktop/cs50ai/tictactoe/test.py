from tictactoe import player, actions, minimax, winner
EMPTY = "None"
X = "X"
O = "O"
grid = [['O', 'O', 'O'], 
        ['X', 'O', 'X'], 
        ['X', 'X', 'O']]


print(winner(grid))
