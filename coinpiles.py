import sys

def can_empty_piles(a, b):
    if (a + b) % 3 == 0 and min(a, b) * 2 >= max(a, b):
        return "YES"
    return "NO"

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    results.append(can_empty_piles(a, b))

sys.stdout.write("\n".join(results) + "\n")
