

'''class Student:
    print("viplove")
Student()    '''

class Student:

    def __init__(self):
        print("this is my default constructor")
        
    def __init__(self,fullname,myage):
       self.name = fullname
       self.age = myage
      
s1 = Student("viplove sana",24) 
print(s1.name,s1.age)

s2 =Student("piyush bhai",22)
print(s2.name,s2.age)
 