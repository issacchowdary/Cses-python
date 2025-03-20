n=int(input())
print(0)
for i in range(2,n+1):
    sqr=i*i
    res=sqr*(sqr-1)
    res=res//2
    mul=4*(i-1)*(i-2)
    res=res-mul
    print(res)

