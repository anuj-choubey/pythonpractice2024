class Numbers :
    def first_number(self):
        self.a =int(input("Enter your first number : "))
        
class Number2 :
    def second_number(self):
        self.b = int(input("Enter your second number : "))
        
class Calculation(Numbers,Number2):
    def addtion(self):
        self.c = self.a+self.b
        print(self.a,"+" ,self.b ,"=",self.c)

    def multiply(self):
        self.c = self.a * self.b
        print(self.a,"*" ,self.b ,"=",self.c)

    def subtract(self):
        self.c = self.a - self.b
        print(self.a,"-" ,self.b ,"=",self.c)

    def gretest_number(self):
        if self.a>self.b:
            print(self.a ,"and",self.b ,"The first number ",self.a,"gretest .")
        elif self.b>self.a:
            print(self.a ,"and" ,self.b ,"The second number ",self.b,"gretest .")
        else:
              print(self.a ,"and" ,self.b ,"Both number Equal ")
    
    def smallest_number(self):
        if self.a<self.b:
            print(self.a ,"and",self.b ,"The first number ",self.a,"smallest .")
        elif self.b<self.a:
            print(self.a ,"and" ,self.b ,"The second number ",self.b,"smallest .")
        else:
              print(self.a ,"and" ,self.b ,"Both number Equal ")
        
ob = Calculation()
ob.first_number()
ob.second_number()
ob.addtion()
ob.multiply()
ob.subtract()
ob.gretest_number()
ob.smallest_number()
