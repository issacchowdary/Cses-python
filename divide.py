import sys

def divide_into_two_sets(n):
    total_sum = n * (n + 1) // 2
    if total_sum % 2 != 0:
        sys.stdout.write("NO\n")
        return
    
    sys.stdout.write("YES\n")
    target = total_sum // 2
    set1, set2 = [], []
    current_sum = 0
    for num in range(n, 0, -1):
        if current_sum + num <= target:
            set1.append(str(num))
            current_sum += num
        else:
            set2.append(str(num))
    sys.stdout.write(f"{len(set1)}\n" + " ".join(set1) + "\n")
    sys.stdout.write(f"{len(set2)}\n" + " ".join(set2) + "\n")

def main():
    n = int(sys.stdin.read().strip())
    divide_into_two_sets(n)

if __name__ == "__main__":
    main()
