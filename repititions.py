s=input()
maxi=0
sumi=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        sumi+=1
    else:
        maxi=max(sumi,maxi)
        sumi=0
maxi=max(maxi,sumi)
print(maxi+1)