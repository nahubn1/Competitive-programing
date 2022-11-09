import numpy as np
from collections import Counter
class Solution:        
    def validTicTacToe(self, board: List[str]) -> bool:
        winner = None
        board = np.array([list(row) for row in board])
        r1, r2, r3 = board[0], board[1], board[2]
        c1, c2, c3 = board[:, 0], board[:, 1], board[:, 2]
        d1, d2 = [board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]
        for i1, i2, i3 in [r1, r2, r3, c1, c2, c3, d1, d2]:
            if i1 == i2 == i3 == 'X':
                winner = 'X'
                break
            elif i1 == i2 == i3 == 'O':
                winner = 'O'
                break
        count = Counter(sum([list(row) for row in board], []))
        if winner == 'X':
            return True if count['X']-count['O'] == 1 else False
        elif winner == 'O':
            return True if count['X']-count['O'] == 0 else False
        else:
            return True if 0 <= count['X']-count['O'] <= 1 else False
