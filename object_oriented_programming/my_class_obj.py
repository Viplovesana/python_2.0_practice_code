

'''class Student:
    print("viplove")
Student()    '''

class Student:
    def __init__(self,fullname,myage):
       self.name = fullname
       self.age = myage
      
s1 = Student("viplove sana",24) 
print(s1.name)
print(s1.age) 