n=int(input())

arr=list(map(int, input().split())) 

total_sum=sum(arr)

min_diff=float('inf')

for mask in range(1<<n):
    subset_sum=sum(arr[i] for i in range(n) if (mask & (1<<i)))
    complement_sum=total_sum-subset_sum
    min_diff=min(min_diff,abs(subset_sum-complement_sum))
print(min_diff)