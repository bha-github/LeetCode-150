class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lvalue = [0]*10
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if lvalue[int(board[i][j])] == 1:
                        return False
                    else:
                        lvalue[int(board[i][j])] = 1
            lvalue = [0]*10
        lvalue = [0]*10
        for j in range(9):
            for i in range(9):
                if board[i][j] != ".":
                    if lvalue[int(board[i][j])] == 1:
                        return False
                    else:
                        lvalue[int(board[i][j])] = 1
            lvalue = [0]*10
        for i in range(0,9,3):
            for j in range(0,9,3):
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != ".":
                            if lvalue[int(board[i+k][j+l])] == 1:
                                return False
                            else:
                                lvalue[int(board[i+k][j+l])] = 1
                lvalue = [0]*10
        return True
                