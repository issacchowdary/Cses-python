
def is_Safe(row,col,cols,diag1,diag2):
    return not (cols[col] or diag1[row+col] or diag2[row-col])

def solve(row,board,cols,diag1,diag2):
    if row==8:
        return 1
    ways=0
    for col in range(8):
        if board[row][col]=='*' or not is_Safe(row,col,cols,diag1,diag2):
            continue
        cols[col]=diag1[row+col]=diag2[row-col]=True
        ways+=solve(row+1,board,cols,diag1,diag2)
        cols[col]=diag1[row+col]=diag2[row-col]=False

    return ways

board=[list(input().strip()) for _ in range(8)]
cols=[False]*8
diag1=[False]*16
diag2=[False]*16

print(solve(0,board,cols,diag1,diag2))

