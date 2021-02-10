"""
Tic Tac Toe Player
"""

import copy
import random

X = "X"
O = "O"
EMPTY = None


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
    if terminal(board):
        return
    elif board == initial_state():
        return X
    else:
        no_of_X = 0
        no_of_O = 0
        for row in board:
            no_of_X += row.count("X")
            no_of_O += row.count("O")

        if (no_of_X > no_of_O):
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actionlist = []

    for (i, row) in enumerate(board):
        for (j, element) in enumerate(row):
            if (element == EMPTY):
                actionlist.append((i, j))

    return actionlist


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    newboard = copy.deepcopy(board)
    turn = player(newboard)
    i, j = action
    newboard[i][j] = turn

    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
        # for checking rows
        for row in board:
            rowset = set(row)
            if None not in rowset and len(rowset) == 1:
                return list(rowset)[0]

        # for checking columns
        transpose_of_board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
        for col in transpose_of_board:
            colset = set(col)
            if None not in colset and len(colset) == 1:
                return list(colset)[0]

        # for checking diagonals
        # Main Diagonal
        maindiagonal = []
        for (i, row) in enumerate(board):
            for (j, element) in enumerate(row):
                if i == j:
                    maindiagonal.append(element)

        maindiagonalset = set(maindiagonal)

        if (None not in maindiagonalset) and (len(maindiagonalset) == 1):
            return maindiagonal[0]

        # Second Diagonal
        seconddiagonal = []
        for (i, row) in enumerate(board):
            for (j, element) in enumerate(row):
                if i + j == 2:
                    seconddiagonal.append(element)

        seconddiagonalset = set(seconddiagonal)

        if (None not in seconddiagonalset) and (len(seconddiagonalset) == 1):
            return seconddiagonal[0]

        # if draw
        s = set()
        for row in board:
            for element in row:
                s.add(element)

        if None not in s:
            return None

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    boardelements = []
    for row in board:
        for element in row:
            boardelements.append(element)

    myset = set(boardelements)

    if len(myset) > 1:

        # for checking rows
        for (i, row) in enumerate(board):
            rowset = set(row)
            if None not in rowset and len(rowset) == 1:
                return True

        # for checking columns
        transpose_of_board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
        for (i, col) in enumerate(transpose_of_board):
            colset = set(col)
            if None not in colset and len(colset) == 1:
                return True

        # for checking diagonals
        # Main Diagonal
        maindiagonal = []
        for (i, row) in enumerate(board):
            for (j, element) in enumerate(row):
                if i == j:
                    maindiagonal.append(element)

        maindiagonalset = set(maindiagonal)

        if (None not in maindiagonalset) and (len(maindiagonalset) == 1):
            return True

        # Second Diagonal
        seconddiagonal = []
        for (i, row) in enumerate(board):
            for (j, element) in enumerate(row):
                if i + j == 2:
                    seconddiagonal.append(element)

        seconddiagonalset = set(seconddiagonal)

        if (None not in seconddiagonalset) and (len(seconddiagonalset) == 1):
            return True

        # if draw
        s = set()
        for row in board:
            for element in row:
                s.add(element)

        if None not in s:
            return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    gamewinner = winner(board)
    if gamewinner == X:
        return 1
    elif gamewinner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    turn = player(board)

    if (turn == O):
        isMin = True
        isMax = False
    else:
        isMax = True
        isMin = False

    totalmaxactions = actions(board)
    if board == initial_state():
        return random.choice(totalmaxactions)

    if (isMin):
        values = []
        for action in totalmaxactions:
            minimumvalue = maxValue(result(board, action), action)
            values.append(minimumvalue)

        return totalmaxactions[values.index(min(values))]

    else:
        values = []
        for action in totalmaxactions:
            maximumvalue = minValue(result(board, action), action)
            values.append(maximumvalue)
        return totalmaxactions[values.index(max(values))]


def maxValue(board, action):
    if terminal(board):
        return utility(board)

    v = -1
    totalmaxactions = actions(board)
    for newaction in totalmaxactions:
        v = max(v, minValue(result(board, newaction), newaction))

    return v


def minValue(board, action):
    if terminal(board):
        return utility(board)

    v = 1
    totalminactions = actions(board)
    for newaction in totalminactions:
        v = min(v, maxValue(result(board, newaction), newaction))

    return v
