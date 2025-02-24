
x=input("enter 1st number")
y=input("enter 2nd number")
sum=0
for t in range (x,y):
    k=len(t)
    n=int(t)

    sum=0
    n=int(t)
    temp=n
    while(n>0):
        r=n%10
        sum+=pow(r,k)
        n=n//10
    print(sum)
    if (temp==sum):
        print("armstrong")
    else:
        print("not armstrong")

