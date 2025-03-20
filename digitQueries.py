
def finddigit(k):
    length=1
    count=9
    start=1

    while k>(length*count):
        k-=length*count
        length+=1
        start*=10
        count*=10
    
    number=start+(k-1)//length
    digit=(k-1)%length
    return str(number)[digit]



t=int(input())
for _ in range(t):
    k=int(input())
    print(finddigit(k))