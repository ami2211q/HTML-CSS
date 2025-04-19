
i=input("enter the number:- ")
b=len(i)
n=int(i)
nn=n
sum=0
r=0
for j in range(b):
    r=n%10
    s=r**b
    sum=sum+s
    n=n//10
if(nn==sum):
    print("armstrong number")
else:
    print("nothing")    