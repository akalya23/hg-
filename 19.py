s2=[]
a=int(input())
b=0
for i in range(2,a+1):
  if(a%i)==0:
    s2.append(i)
for i in s1:
  b=0
  for j in range(1,i+1,1):
    if (i%j)==0:
      b=b+1
  if b==2:
    print (i,end=" ")
