# n = int(input("Enter a number : "))

class Palendrome:
    def __init__(self):
        pass
    
    def check_palendrome(self, number):
        n = number
        temp = n
        rev = 0
        while n>0:
            r = n%10
            rev = (rev *10) +r
            n = n//10

        if rev == temp:
            print(temp, "is prime number")
        else:
            print("not")
                
    def get_all_palendrome(self, from_number, to_number):
    
        if from_number>to_number:
            big = from_number
            small = to_number
        else :
            big  = to_number
            small = from_number
            

        while small <= big:
            n = small
            temp = n
            rev = 0
            while n>0:
                r = n%10
                rev = (rev *10) +r
                n = n//10

            if rev == temp:
                print(temp)
            # else:
                # print("not")

            small = small +1
choice = int(input('''Select program number to run
1: Check palendrome number
2: Get all palendrome between given range'''))
pal_obj = Palendrome()
if choice == 1:
    n = int(input("Enter first number "))
    pal_obj.check_palendrome(n)
elif choice == 2:
    n1 = int(input("Enter first number "))
    n2 = int(input("Enter second number "))
    pal_obj.get_all_palendrome(n1, n2)
else:
    print("Invalid Choice")
