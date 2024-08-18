# intiate a class
class Employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print(id(self))
        self.age = 21
        self.salray = 30000
        self.id = 100
    
    def travel(self,des):
        print(f"employee is travelling to {des}")

# creating an instance/object of the class
prajun = Employee()
print(id(prajun))

# printing the attributes
# print(prajun.age)

# calling the methods
prajun.travel('home')