n=int(input())
ans = list(map(int, input().split())) 
rsum=n*(n+1)
rsum//=2
sum=sum(ans)
print(rsum-sum)
