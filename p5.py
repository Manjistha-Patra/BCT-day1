#prime number
p=int(input("enter the number :"))
temp=0
for i  in range (2,p):
     if(p%i==0):
         temp=1
         break
if(temp==1):
    print("not prime")
else:
    print("prime")

   
    
