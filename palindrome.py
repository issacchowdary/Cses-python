from collections import Counter

s = input().strip()
freq = Counter(s)
odd_count = sum(1 for v in freq.values() if v % 2 == 1)

if odd_count > 1:
    print("NO SOLUTION")
else:
    first_half, middle = [], ""
    for char, count in sorted(freq.items()):
        if count % 2 == 1:
            middle = char * count
        else:
            first_half.append(char * (count // 2))
    
    first_half = "".join(first_half)
    print(first_half + middle + first_half[::-1])
