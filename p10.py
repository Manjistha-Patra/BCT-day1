#fibo
n=int(input("enter the number terms"))
n1=0
n2=1
print("fibonacci series :", n1, n2)
for i in range (2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)