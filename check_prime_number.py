n = int(input("Enter Your number "))
i=1
r = 0
count = 0
while i<=n:
    r = n%i
    if r == 0:      
        count = count +1
    i = i+1   
if count ==2 :
    print("this is a prime number ")
else:
    print("not")
