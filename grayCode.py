n=int(input())
items=[(i^(i>>1)) for i in range(1<<n)]
for item in items:
    print(f"{item:0{n}b}")