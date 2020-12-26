class Student:
    """ This class stores data of a student"""
    clas = "TE"
    def __init__(self, name="", roll=0, age=0):
        self.name = name
        self.age = age
        self.roll = roll
    
    def older(self, inc, ince):
        self.age += inc
        self.clas += ince 
        

s1 = Student("Ravi", 6, 18)
print(s1.age)
s1.older(3, "ELEX")
print(s1.age, s1.clas)
s2 = Student()
print(s2.clas)  
