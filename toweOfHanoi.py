
def hanoi(n,strt,aux,dest,moves):
    if n==1:
        moves.append((strt,dest))
        return
    hanoi(n-1,strt,dest,aux,moves)
    moves.append((strt,dest))
    hanoi(n-1,aux,strt,dest,moves)

def solve(n):
    moves=[]
    hanoi(n,1,2,3,moves)
    print(len(moves))
    for move in moves:
        print(*move)
n=int(input())
solve(n)