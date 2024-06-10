
class Number:
    def val(self,val=None):
         self.first_num = val if val is not None else int(input("enter number : "))
         return self.first_num
            
class Addtion(Number):
    def add(self):
       print(self.first_num **2)

class Cube(Number):
    def cubee(self):
        print(self.first_num **3)


cube = Cube()
addtion = Addtion()
addtion.val(cube.val())
cube.cubee()

addtion.add()
