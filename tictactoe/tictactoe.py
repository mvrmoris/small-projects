"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY ='None'


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    if terminal(board):
        return None

    for i in board:
        for j in i:
            if j == X:
                x_count += 1
            elif j == O:
                o_count += 1
    if x_count == 0 or x_count == o_count: 
        return X
    if x_count > o_count:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    if terminal(board):
        return None
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if action not in actions(board):
        raise Exception
    else:
        turn = player(board)
        new_board[action[0]][action[1]] = turn 

    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #checking rows
    for i in board: 
        x_count = 0
        o_count = 0
        for j in i:
            if j == X:
                x_count += 1
            
            if x_count == 3:
                return X
            elif j == O:
                o_count += 1
            if o_count == 3:
                return O
    
        

    #checking columns
    j = 0
    i = 0
    x_count = 0
    o_count = 0
    while i < len(board):
        
        if board[j][i] == X:
            x_count += 1
    
        if x_count == 3:
            return X
        if board[j][i] == O:
            o_count += 1
        if o_count == 3:
            return O
        
        j += 1
        if j == 3:
            x_count = 0
            o_count = 0
            j = 0
            i += 1
    

    #checking diagonal
    x_count = 0
    o_count = 0
    i = 0
    for i in range(len(board)):
        if board[i][i] == X:
            x_count += 1
        if board[i][i] == O:
            o_count += 1

        if o_count == 3:
            return O

        if x_count == 3:
            return X

    i = 2
    j = 0
    x_count = 0
    o_count = 0
    while i >= 0:
        if board[j][i]==X:
            x_count += 1

        if board[j][i] == O:
            o_count += 1
        j += 1
        i -= 1
        if x_count == 3: 
            return X
        if o_count == 3:
            return O
        
        

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
    
        return True

    for i in board:
        for j in i:
            
            
            if j == EMPTY:
                
                return False
    return True
    
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0
    


def minimax(board):
    """
    x tries to maximize the score and o to minimize it 
    Returns the optimal action for the current player on the board.
    """
    Min = float('-inf')
    Max = float('inf')
    print(actions(board))
    if terminal(board):
        return None
    if player(board) == X:
        return (max_value(board,Min,Max)[1])
    else:
        return (min_value(board,Min,Max)[1])


def max_value(board,Max,Min):
    
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float('-inf')
    for action in actions(board):
        test =min_value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]
            
def min_value(board,Max,Min):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float('inf')
    for action in actions(board):
        test = max_value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]




    
