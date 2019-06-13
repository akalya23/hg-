s1=input().split()
b=[]
for i in s1:
    b.append(i[::-2])
print(*b)
