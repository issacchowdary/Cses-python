# from collections import Counter
# from itertools import permutations

# def generate(str):
#     unique=sorted(set(permutations(str)))
#     print(len(unique))
#     for uni in unique:
#         print("".join(uni))

# str=input().strip()
# generate(str)

def permute(s,l,r,unique_permutations):
    if l==r:
        unique_permutations.add("".join(s))
        return
    for i in range(l,r+1):
        s[l],s[i]=s[i],s[l]
        permute(s,l+1,r,unique_permutations)
        s[l],s[i]=s[i],s[l]

def generate_string(str):
    unique_permutations=set()
    permute(list(str),0,len(str)-1,unique_permutations)
    sorted_permutations=sorted(unique_permutations)
    print(len(sorted_permutations))
    for perm in sorted_permutations:
        print(perm)

str=input().strip()
generate_string(str)

