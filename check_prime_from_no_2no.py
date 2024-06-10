n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))
if n1>n2:
    big = n1
    small = n2
else :
    big  = n2
    small = n1
    

while small <= big:
    i=1
    count = 0
    while i<=small:
        r = small%i
        if r == 0:      
            count = count +1
        i = i+1   
    if count ==2 :
        print(small, ",", end="")
    # else:
        # print("not")

    small = small +1
