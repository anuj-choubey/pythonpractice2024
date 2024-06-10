num = int(input("Enter your number "))
temp = num
summ = 0
count = 0
while temp>0:
    r = temp % 10
    temp= int(temp/10)
    summ = summ+r
    count = count + 1
print("Sum of all digits in number",num,"is" ,summ)
print("Digits in number",num,"is" ,count)
    
