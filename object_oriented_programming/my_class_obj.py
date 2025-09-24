

'''class Student:
    print("viplove")
Student()    '''

'''class Student:

    def __init__(self):
        print("this is my default constructor")
        
    def __init__(self,fullname,myage):
       self.name = fullname
       self.age = myage
      
s1 = Student("viplove sana",24) 
print(s1.name,s1.age)

s2 =Student("piyush bhai",22)
print(s2.name,s2.age)'''


class Student:
    def __init__(self,fullname,myage):
        self.name = fullname
        self.age = myage

    def say_hello(self):
        print("hello",self.name)

    def say_bye(self):
        return self.name     

s1 = Student("viplove",24)
print (s1.name,s1.age)

s1.say_hello()
print(s1.say_bye())



 