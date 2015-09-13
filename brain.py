def next(board, turn):
    for i in xrange(3):
        for j in xrange(3):
            if board[i][j] == None:
                board[i][j] = turn
                yield board, (i, j)
                board[i][j] = None


def row_check(board, i):
    return board[i][0] == board[i][1] and board[i][1] == board[i][2]

def col_check(board, i):
    return board[0][i] == board[1][i] and board[1][i] == board[2][i]

def diag_check(board, direction):
    if direction == 0:
        return board[0][0] == board[1][1] and board[1][1] == board[2][2]
    else:
        return board[0][2] == board[1][1] and board[1][1] == board[2][0]

def draw(board):
    for i in xrange(3):
        for j in xrange(3):
            if board[i][j] == None:
                return False
    return True

def check(board):
    # return 1 if we have won.
    # return -1 if we have lost.
    # else None.

    # check rows.
    for i in xrange(3):
        if board[i][0] != None:
            player = board[i][0]
            won = row_check(board, i)
            if won:
                return 1 if player == 1 else -1

    # check columns.
    for i in xrange(3):
        if board[0][i] != None:
            player = board[0][i]
            won = col_check(board, i)
            if won:
                return 1 if player == 1 else -1

    # check diagonals.
    if board[0][0] != None:
        player = board[0][0]
        won = diag_check(board, 0)
        if won:
            return 1 if player == 1 else -1
    if board[0][2] != None:
        player = board[0][2]
        won = diag_check(board, 1)
        if won:
            return 1 if player == 1 else -1
    return None


def evaluate(board, turn):
    res = check(board)
    if res != None:
        return res

    if draw(board):
        return 0

    if turn == 1:
        # max node.
        ans = -1
        moves = next(board, turn)
        for move in moves:
            sol = evaluate(move[0], 0)
            ans = max(ans, sol)
        return ans
    else:
        # min node.
        ans = 1
        moves = next(board, turn)
        for move in moves:
            sol = evaluate(move[0], 1)
            ans = min(ans, sol)
        return ans

def best_move(board):
    moves = next(board, 1)
    ans = -1
    best = None
    for move in moves:
        sol = evaluate(move[0], 0)
        if sol > ans:
            ans = sol
            best = move[1]

        elif best == None:
            ans = sol
            best = move[1]
    return best
